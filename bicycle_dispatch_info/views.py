import json

from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from bicycle.models import Bicycle
from bicycle_dispatch_info.forms import AddBicycleDispatchInfoForm, AlterBicycleDispatchInfoForm
from bicycle_dispatch_info.models import BicycleDispatchInfo
from utils.form_helper import verify_form


class AddBicycleDispatchInfoView(View):

    def post(self, request, bicycle_num):
        str = request.body.decode()
        data_dict = json.loads(str)
        data, status = verify_form(AddBicycleDispatchInfoForm, data_dict)
        if not status:
            return JsonResponse(status=204, data=data)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        try:
            BicycleDispatchInfo.objects.get(remote_record_id=data['remote_record_id'])
            return JsonResponse(status=204, data={'errors':[
                {'resource': 'bicycle_transfer_record', 'code': 'already exists'}
            ]})
        except BicycleDispatchInfo.DoesNotExist:
            pass
        dispatch_data = {}
        dispatch_data['remote_record_id'] = data['remote_record_id']
        dispatch_data['company_id'] = bicycle_num
        dispatch_data['company_name'] = bicycle_num
        dispatch_data['dispatch_status'] = data['transfer_status']
        dispatch_data['dispatcher'] = data['transfer_user']
        dispatch_data['dispatcher_phone'] = data['transfer_user_tele']
        dispatch_data['dispatch_start_lon'] = data['transfer_start_lon']
        dispatch_data['dispatch_start_lat'] = data['transfer_start_lat']
        dispatch_data['dispatch_end_lon'] = data['transfer_end_lon']
        dispatch_data['dispatch_end_lat'] = data['transfer_end_lat']
        dispatch_data['dispatch_start_time'] = data['transfer_start_time']
        dispatch_data['dispatch_end_time'] = data['transfer_end_time']
        dispatch_data['dispatch_start_addr'] = data['transfer_start_position']
        dispatch_data['dispatch_end_addr'] = data['transfer_end_position']
        BicycleDispatchInfo.objects.create(**dispatch_data)
        return HttpResponse(status=204)


class AlterBicycleDispatchInfoView(View):
    def post(self, request, bicycle_num, remote_record_id):
        str = request.body.decode()
        data_dict = json.loads(str)
        data, status = verify_form(AlterBicycleDispatchInfoForm, data_dict)
        if not status:
            return JsonResponse(status=204, data=data)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        try:
            bdi = BicycleDispatchInfo.objects.get(remote_record_id=remote_record_id)
        except BicycleDispatchInfo.DoesNotExist:
            return HttpResponseNotFound()
        bdi.dispatch_status = data['transfer_status']
        bdi.dispatcher = data['transfer_user']
        bdi.dispatcher_phone = data['transfer_user_tele']
        bdi.dispatch_start_lon = data['transfer_start_lon']
        bdi.dispatch_start_lat = data['transfer_start_lat']
        bdi.dispatch_end_lon = data['transfer_end_lon']
        bdi.dispatch_end_lat = data['transfer_end_lat']
        bdi.dispatch_start_time = data['transfer_start_time']
        bdi.dispatch_end_time = data['transfer_end_time']
        bdi.dispatch_start_addr = data['transfer_start_position']
        bdi.dispatch_end_addr = data['transfer_end_position']
        bdi.save()
        return HttpResponse(status=204)