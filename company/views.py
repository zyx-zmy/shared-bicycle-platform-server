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
from company.forms import CompanyForm, CompanysForm
# Create your views here.

class CompanyView(View):
	
	@session_required()
	def get(self, request, company_id):
		try:
			record = Company.objects.get(company_id=company_id)
		except Company.DoesNotExist:
			return HttpResponseNotFound()
		return HttpJsonResponse(record.detail_info())

	@session_required()
	def put(self, request, company_id):
		flag, data = validate_form(CompanyForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
		record = Company.objects.filter(company_id=company_id)
		if not record.exists():
			return HttpResponseNotFound()
		record.update(**data)
		return HttpJsonResponse(status=204)

class CompanysView(View):

	@session_required()
	def get(self, request):
		flag, data = validate_form(CompanysForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
		q = Q()
		if data["company_name"]:
			q &= Q(company_name__icontains=data["company_name"])
		if data["start_time"]:
			q &= Q(created_time__gte=ttd(data["start_time"]))
		if data["end_time"]:
			q &= Q(created_time__lte=ttd(data["end_time"]))
		responses = Company.objects.filter(q).order_by("-created_time")
		responses_count = len(responses)
		responses = Paginator(responses, data['page_size'])
		responses = responses.page(data['page_num'])
		responses = [res.detail_info() for res in responses]
		response = HttpJsonResponse(responses)
		next_page = True if responses_count > data['page_size'] * data['page_num'] else False
		if next_page:
			params = 'page_num=%d&page_size=%d' % (data['page_num'] + 1, data['page_size'])
			if data['company_name']:
				params += '&company_name=%s' % (data['company_name'])
			if data['start_time']:
				params += '&start_time=%s' % data['start_time']
			if data['end_time']:
				params += '&end_time=%s' % data['end_time']
			response['Link'] = r'<%s%s?%s>; rel="next"' % (
				get_local_host(request), request.path, params)
		return response

	@session_required()
	def post(self, request):
		flag, data = validate_form(CompanyForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
		record = Company.objects.create(**data)
		return HttpJsonResponse({
			"company_id": record.order_id,
			"created_time": dtt(record.created_time),
			}, status=201)