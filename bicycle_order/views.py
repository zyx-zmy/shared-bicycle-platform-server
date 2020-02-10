import json

from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from bicycle.models import Bicycle
from bicycle_order.forms import AddBicycleOrderForm, AlterBicycleOrderForm
from bicycle_order.models import BicycleOrder
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.helper import HttpJsonResponse


class AddBicycleOrderView(View):
    @bicycle_client_required()
    def post(self, request, bicycle_num):
        status, data = validate_form(AddBicycleOrderForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        order_dict = {}
        order_dict['bicycle_order_id'] = data['remote_order_id']
        order_dict['bicycle_number'] = bicycle_num
        order_dict['company_id'] = request.company_id
        order_dict['user_id'] = data['user_num']
        order_dict['start_time'] = data['start_time']
        order_dict['end_time'] = data['end_time']
        order_dict['start_lon'] = data['start_lon']
        order_dict['start_lat'] = data['start_lat']
        order_dict['start_addr'] = data['start_position']
        order_dict['end_lon'] = data['end_lon']
        order_dict['end_lat'] = data['end_lat']
        order_dict['end_addr'] = data['end_position']
        order_dict['driving_distance'] = data['distance']
        BicycleOrder.objects.create(**order_dict)
        return HttpResponse(status=204)


class AlterBicycleOrderView(View):
    @bicycle_client_required()
    def post(self, request, bicycle_num, remote_order_id):
        status, data = validate_form(AlterBicycleOrderForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        try:
            b_order = BicycleOrder.objects.get(bicycle_order_id=remote_order_id)
        except BicycleOrder.DoesNotExist:
            return HttpResponseNotFound()
        b_order.bicycle_num = bicycle_num
        b_order.user_id = data['user_num']
        b_order.start_time = data['start_time']
        b_order.end_time = data['end_time']
        b_order.start_lon = data['start_lon']
        b_order.start_lat = data['start_lat']
        b_order.start_addr = data['start_position']
        b_order.end_lon = data['end_lon']
        b_order.end_lat = data['end_lat']
        b_order.end_addr = data['end_position']
        b_order.driving_distance = data['distance']
        b_order.save()
        return HttpResponse(status=204)