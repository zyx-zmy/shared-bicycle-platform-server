import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from bicycle.models import Bicycle
from bicycle_event.forms import AddBicycleEventForm, AlterBicycleEventForm, GetBicycleEventForm
from bicycle_event.models import BicycleEvent
from company.models import Company
from user.models import User
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.decorators import session_required
from utils.helper import HttpJsonResponse, get_local_host


class AddBicycleEvent(View):
    @bicycle_client_required()
    def post(self, request, bicycle_num):
        status, data = validate_form(AddBicycleEventForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        try:
            user = User.objects.get(user_id=data['user_num'])
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        event_dict = {}
        event_dict['bicycle_event_id'] = data['remote_event_id']
        event_dict['bicycle_number'] = bicycle_num
        event_dict['company_id'] = request.company_id
        event_dict['user'] = user
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
    @bicycle_client_required()
    def post(self, request, bicycle_num, remote_event_id):
        status, data = validate_form(AlterBicycleEventForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
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

class GetBicycleEvent(View):
    @session_required()
    def get(self, request):
        flag, data = validate_form(GetBicycleEventForm, request.jsondata)
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
        if data["event_type"]:
            q &= Q(event_type=data["event_type"])
        responses = BicycleEvent.objects.filter(q).order_by("-updated_time")
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
            if data['event_type']:
                params += '&event_type=%s' % data['event_type']
            if data['bicycle_number']:
                params += '&bicycle_number=%s' % data['bicycle_number']
            if data['user_id']:
                params += '&user_id=%s' % data['user_id']
            response['Link'] = r'<%s%s?%s>; rel="next"' % (
                get_local_host(request), request.path, params)
        return response