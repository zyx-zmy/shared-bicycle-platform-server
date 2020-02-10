import json

from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from bicycle.forms import AddBicycleForm, AlterBicycleForm
from bicycle.models import Bicycle
from utils.forms import validate_form


class AddBicycle(View):

    def post(self, request):
        str = request.body.decode()
        data_dict = json.loads(str)
        status, data = validate_form(AddBicycleForm, data_dict)
        if not status:
            return JsonResponse(status=204,data=data)
        # todo 车辆类型去备案取
        # data['bicycle_type'] =

        Bicycle.objects.create(**data)
        return HttpResponse(status=204)


class AlterBicycle(View):

    def post(self, request, bicycle_num):
        print(111)
        str = request.body.decode()
        data_dict = json.loads(str)
        status, data = validate_form(AlterBicycleForm, data_dict)
        if not status:
            return JsonResponse(status=204,data=data)
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
