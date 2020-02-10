import time
import datetime
import math
import json
import threading
import itertools
import urllib.request
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseForbidden
from django.db.models import Q
from django.views.generic import View
from utils.datetime_utils import dtt, ttd
from utils.forms import validate_form
from utils.responses import HttpJsonResponse
from utils.decorators import session_required, json_required, operation_session_required
from utils.helper import get_local_host
from functools import reduce
from company.models import Company
from bicycle_beian.models import BicycleBeian, BicycleNumber
from bicycle_beian.forms import BicycleBeianForm, BicycleBeianCreateForm, BicycleNumberGetForm, BicycleBeianAccessNumForm

# Create your views here.
class BicyclesBeianView(View):

	@session_required()
	def get(self, request):
		flag, data = validate_form(BicycleBeianForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
		q = Q()
		if data["company_name"]:
			company = Company.objects.filter(company_name__icontains=data["company_name"])
			ids = [x.company_id for x in company]
			q &= Q(company_id__in=ids)
		if data["start_time"]:
			q &= Q(created_time__gte=ttd(data["start_time"]))
		if data["end_time"]:
			q &= Q(created_time__lte=ttd(data["end_time"]))
		responses = BicycleBeian.objects.filter(q).order_by("-created_time")
		return HttpJsonResponse([x.detail_info() for x in responses])

	@session_required
	def post(self, request):
		flag, data = validate_form(BicycleBeianCreateForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
		try:
			company = Company.objects.get(company_id=data["company_id"])
		except Company.DoesNotExist:
			return HttpResponseNotFound()
		record = BicycleBeian.objects.create(**data)
		return HttpJsonResponse({
				"beian_bicycle_id": record.beian_bicycle_id,
				"created_time": dtt(record.created_time)
		}, status=201)

class BicycleBeianView(View):

	@session_required()
	def get(self, request, beian_bicycle_id):
		try: 
			bicycle = BicycleBeian.objects.get(beian_bicycle_id=beian_bicycle_id)
		except BicycleBeian.DoesNotExist:
			return HttpResponseNotFound()
		return HttpJsonResponse(bicycle.detail_info())

	@session_required()
	def put(self, request, beian_bicycle_id):
		flag, data = validate_form(BicycleBeianCreateForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)		
		try:
			company = Company.objects.get(company_id=data["company_id"])
		except Company.DoesNotExist:
			return HttpResponseNotFound()
		record = BicycleBeian.objects.filter(beian_bicycle_id=beian_bicycle_id)
		if not record.exists():
			return HttpResponseNotFound()
		record.update(**data)
		return HttpJsonResponse(status=204)

	@session_required()
	def patch(self, request, beian_bicycle_id):
		flag, data = validate_form(BicycleBeianAccessNumForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)		
		try:
			bicycle = BicycleBeian.objects.get(beian_bicycle_id=beian_bicycle_id)
		except BicycleBeian.DoesNotExist:
			return HttpResponseNotFound()
		bicycle.access_num = data["access_num"]
		bicycle.save()
		return HttpJsonResponse(status=204)

class BicycleNumbersView(View):

	@session_required()
	def post(self, request, beian_bicycle_id):
		try: 
			bicycle = BicycleBeian.objects.get(beian_bicycle_id=beian_bicycle_id)
		except BicycleBeian.DoesNotExist:
			return HttpResponseNotFound()
		try:
			company = Company.objects.get(company_id=bicycle.company_id)
		except Company.DoesNotExist:
			return HttpResponseNotFound()
		number_file = request.FILES.get('number_file')
		if not number_file:
			return HttpJsonResponse({
				"message": "Validation Failed",
				"errors": [
					{"field": "FILE", "code": "invalid"},
				]
			}, status=422)
		err = []
		i = 0
		j = 0
		index = number_file.name.rfind('.')
		ext = number_file.name[index:]
		header_row = ['车辆编号']
		if ext not in ['.csv', '.xlsx']:
			return HttpJsonResponse({
				"message": "Validation Failed",
				"errors": [
					{"resource": "FILE", "code": "incorrect_format"},
				]
			}, status=422)
		content_iter_cars = iter([])
		try:
			if ext == '.csv':
				content = [row.split(',') for row in number_file.read().decode('utf-8').split('\n')]
				content_iter_cars = iter(content)
				content_length = len(content)
			elif ext == '.xlsx':
				content = pyexcel.get_sheet(
					file_type='xlsx', file_content=number_file.read()
				).array
				content_length = len(content)
				content_iter_cars = iter(content)
			else:
				content_length = 0
		except Exception as e:
			return HttpJsonResponse({
				"message": "Validation Failed",
				"errors": [
					{"field": "FILE", "code": "invalid"},
				]
			}, status=422)
		if content_length > bicycle.access_num:
			return HttpJsonResponse({
				"message": "Validation Failed",
				"errors": [
					{"resource": "FILE", "code": "access_num"}
				]
			}, status=422)
		if content_length - 1 > 5000:
			return HttpJsonResponse({
				"message": "Validation Failed",
				"errors": [
					{"resource": "FILE", "code": "scale_out"}
				]
			}, status=422)
		if next(content_iter_cars) != header_row:
			return HttpJsonResponse({
				"message": "Validation Failed",
				"errors": [
					{"resource": "FILE", "code": "incorrect_format"},
				]
			}, status=422)
		for item in content_iter_cars:
			j += 1
			i += 1
			try:
				with transaction.atomic():
					BicycleNumber.objects.get_or_create(
						bicycle_number=item[0],
						bicycle_id=bicycle.beian_bicycle_id,
						company_id=company.company_id,
					)
			except Exception as e:
				logger.debug('数据创建问题:%s' % e)
				err.append(j)
				i -= 1
				continue
		bicycle.has_bicycle_number = True
		bicycle.save()
		return HttpJsonResponse({
			"success": i,
			"failed": content_length - i - 1,
			"err_row": err
		}, status=201)

	@session_required()
	def delete(self, request, beian_bicycle_id):
		try:
			record = BicycleBeian.objects.get(beian_bicycle_id=beian_bicycle_id)
		except BicycleBeian.DoesNotExist:
			return HttpResponseNotFound()
		BicycleNumber.objects.filter(beian_bicycle_id=beian_bicycle_id).delete()
		record.has_bicycle_number = True
		record.save()
		return HttpJsonResponse(status=204)

	@session_required()
	def get(self, request, beian_bicycle_id):
		flag, data = validate_form(BicycleNumberGetForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
		try:
			record = BicycleBeian.objects.get(beian_bicycle_id=beian_bicycle_id)
		except BicycleBeian.DoesNotExist:
			return HttpResponseNotFound()
		responses = BicycleNumber.objects.filter(beian_bicycle_id=beian_bicycle_id)
		responses_count = len(responses)
		responses = Paginator(responses, data['page_size'])
		responses = responses.page(data['page_num'])
		responses = [res.detail_info() for res in responses]
		response = HttpJsonResponse(responses)
		next_page = True if responses_count > data['page_size'] * data['page_num'] else False
		if next_page:
			params = 'page_num=%d&page_size=%d' % (data['page_num'] + 1, data['page_size'])
			response['Link'] = r'<%s%s?%s>; rel="next"' % (
				get_local_host(request), request.path, params)
		return response