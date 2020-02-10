import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from bicycle.forms import AddBicycleForm, AlterBicycleForm, BicycleForm
from bicycle.models import Bicycle
from bicycle_beian.models import BicycleBeian
from company.models import Company
from utils.decorators import session_required
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.helper import HttpJsonResponse, get_local_host


class AddBicycle(View):
    @bicycle_client_required()
    def post(self, request):
        status, data = validate_form(AddBicycleForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        try:
            bicycle_type_num = BicycleBeian.objects.get(bicycle_model_code=data['bicycle_type_num']).bicycle_type
        except BicycleBeian.DoesNotExist:
            return HttpResponseNotFound()
        data['bicycle_type'] = bicycle_type_num
        data['company_id'] = request.company_id
        Bicycle.objects.create(**data)
        return HttpResponse(status=204)


class AlterBicycle(View):
    @bicycle_client_required()
    def post(self, request, bicycle_num):
        status, data = validate_form(AlterBicycleForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        try:
            bicycle = Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        bicycle.bicycle_type_num = data['bicycle_type_num']
        bicycle.location_type = data['location_type']
        bicycle.bluetooth_mac = data['bluetooth_mac']
        bicycle.frame_number = data['frame_number']
        bicycle.production_time = data['production_time']
        bicycle.first_put_time = data['first_put_time']
        bicycle.last_put_time = data['last_put_time']
        bicycle.last_put_lon = data['last_put_lon']
        bicycle.last_put_lat = data['last_put_lat']
        bicycle.last_put_position = data['last_put_position']
        bicycle.repair_count = data['repair_count']
        bicycle.last_repair_time = data['last_repair_time']
        bicycle.last_recovery_time = data['last_recovery_time']
        bicycle.put_status = data['put_status']
        bicycle.save()
        return HttpResponse(status=204)

class BicycleView(View):
	@session_required()
	def get(self, request):
		flag, data = validate_form(BicycleForm, request.jsondata)
		if not flag:
			return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
		q = Q()
		if data["company_name"]:
			company = Company.objects.filter(company_name__icontains=data["company_name"])
			ids = [x.company_id for x in company]
			q &= Q(company_id__in=ids)
		if data["bicycle_num"]:
			q &= Q(bicycle_num=data["bicycle_num"])
		if data["bicycle_type_num"]:
			q &= Q(bicycle_type_num=data["bicycle_type_num"])
		if data["bicycle_type"]:
			q &= Q(bicycle_type=data["bicycle_type"])
		if data["put_status"]:
			q &= Q(put_status=data["put_status"])
		responses = Bicycle.objects.filter(q).order_by("-updated_time")
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
			if data['bicycle_num']:
				params += '&bicycle_num=%s' % data['bicycle_num']
			if data['bicycle_type_num']:
				params += '&bicycle_type_num=%s' % data['bicycle_type_num']
			if data['bicycle_type']:
				params += '&bicycle_type=%s' % data['bicycle_type']
			if data['put_status']:
				params += '&put_status=%s' % data['put_status']
			response['Link'] = r'<%s%s?%s>; rel="next"' % (
				get_local_host(request), request.path, params)
		return response

class BicyclesView(View):
	@session_required()
	def get(self, request, bicycle_id):
		try:
			record = Bicycle.objects.get(bicycle_id=bicycle_id)
		except Bicycle.DoesNotExist:
			return HttpResponseNotFound()
		return HttpJsonResponse(record.detail_info())