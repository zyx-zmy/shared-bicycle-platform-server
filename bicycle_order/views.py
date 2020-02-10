import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from company.models import Company
from user.models import User
from utils.decorators import session_required
from bicycle.models import Bicycle
from bicycle_order.forms import AddBicycleOrderForm, AlterBicycleOrderForm, GetBicycleOrderForm
from bicycle_order.models import BicycleOrder
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.helper import HttpJsonResponse, get_local_host


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

class BicycleOrderView(View):
    @session_required()
    def get(self, request, bicycle_order_id):
        try:
            record = BicycleOrder.objects.get(bicycle_order_id=bicycle_order_id)
        except BicycleOrder.DoesNotExist:
            return HttpResponseNotFound()
        return HttpJsonResponse(record.detail_info())

class BicycleOrdersView(View):
    @session_required()
    def get(self, request):
        flag, data = validate_form(GetBicycleOrderForm, request.jsondata)
        if not flag:
            return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
        q = Q()
        if data["company_id"]:
            try:
                company = Company.objects.get(company_id=data["company_id"])
            except Company.DoesNotExist:
                return HttpJsonResponse([])
            q &= Q(company=company)
        if data["bicycle_number"]:
            q &= Q(bicycle_number=data["bicycle_number"])
        if data["user_id"]:
            try:
                user = User.objects.get(user_id=data['user_id'])
            except User.DoesNotExist:
                return HttpJsonResponse([])
            q &= Q(user=user)
        if data["bicycle_order_id"]:
            q &= Q(bicycle_order_id=data["bicycle_order_id"])
        responses = BicycleOrder.objects.filter(q).order_by("-updated_time")
        responses_count = len(responses)
        responses = Paginator(responses, data['page_size'])
        responses = responses.page(data['page_num'])
        responses = [res.detail_info() for res in responses]
        response = HttpJsonResponse(responses)
        next_page = True if responses_count > data['page_size'] * data['page_num'] else False
        if next_page:
            params = 'page_num=%d&page_size=%d' % (data['page_num'] + 1, data['page_size'])
            if data['company_id']:
                params += '&company_id=%s' % (data['company_id'])
            if data['bicycle_number']:
                params += '&bicycle_number=%s' % data['bicycle_number']
            if data['user_id']:
                params += '&user_id=%s' % data['user_id']
            if data['bicycle_order_id']:
                params += '&bicycle_order_id=%s' % data['bicycle_order_id']
            response['Link'] = r'<%s%s?%s>; rel="next"' % (
                get_local_host(request), request.path, params)
        return response