import json

from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from bicycle.models import Bicycle
from bicycle_event.forms import AddBicycleEventForm, AlterBicycleEventForm
from bicycle_event.models import BicycleEvent
from user.models import User
from utils.forms import validate_form


class AddBicycleEvent(View):
    def post(self, request, bicycle_num):
        str = request.body.decode()
        data_dict = json.loads(str)
        status, data = validate_form(AddBicycleEventForm, data_dict)
        if not status:
            return JsonResponse(status=204, data=data)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        try:
            User.objects.get(user_id=data['user_num'])
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        event_dict = {}
        event_dict['bicycle_event_id'] = data['remote_event_id']
        event_dict['bicycle_number'] = bicycle_num
        event_dict['company_id'] = bicycle_num
        event_dict['company_name'] = bicycle_num
        event_dict['user_id'] = data['user_num']
        event_dict['event_type'] = data['event_type']
        event_dict['bicycle_order_id'] = data['bicycle_order_id']
        event_dict['start_time'] = data['start_time']
        event_dict['end_time'] = data['end_time']
        event_dict['start_lon'] = data['start_lon']
        event_dict['start_lat'] = data['start_lat']
        event_dict['start_addr'] = data['start_position']
        event_dict['end_lon'] = data['end_lon']
        event_dict['end_lat'] = data['end_lat']
        event_dict['end_addr'] = data['end_position']
        BicycleEvent.objects.create(**event_dict)
        return HttpResponse(status=204)

class AlterBicycleEvent(View):
    def post(self, request, bicycle_num, remote_event_id):
        str = request.body.decode()
        data_dict = json.loads(str)
        status, data = validate_form(AlterBicycleEventForm, data_dict)
        if not status:
            return JsonResponse(status=204, data=data)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        try:
            b_event = BicycleEvent.objects.get(bicycle_event_id=remote_event_id)
        except BicycleEvent.DoesNotExist:
            return HttpResponseNotFound()
        b_event.user_id = data['user_num']
        b_event.event_type = data['event_type']
        b_event.bicycle_order_id = data['bicycle_order_id']
        b_event.start_time = data['start_time']
        b_event.end_time = data['end_time']
        b_event.start_lon = data['start_lon']
        b_event.start_lat = data['start_lat']
        b_event.start_addr = data['start_position']
        b_event.end_lon = data['end_lon']
        b_event.end_lat = data['end_lat']
        b_event.end_addr = data['end_position']
        b_event.save()
        return HttpResponse(status=204)