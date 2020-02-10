import json

from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from bicycle.forms import AddBicycleForm, AlterBicycleForm
from bicycle.models import Bicycle
from bicycle_beian.models import BicycleBeian
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.helper import HttpJsonResponse


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
