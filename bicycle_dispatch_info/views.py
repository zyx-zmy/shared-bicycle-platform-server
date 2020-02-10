import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from company.models import Company
from utils.decorators import session_required
from bicycle.models import Bicycle
from bicycle_dispatch_info.forms import AddBicycleDispatchInfoForm, AlterBicycleDispatchInfoForm,\
    GetBicycleDispatchInfoForm
from bicycle_dispatch_info.models import BicycleDispatchInfo
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.helper import HttpJsonResponse, get_local_host


class AddBicycleDispatchInfoView(View):

    @bicycle_client_required()
    def post(self, request, bicycle_num):
        status, data = validate_form(AddBicycleDispatchInfoForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
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
        dispatch_data['company_id'] = request.company_id
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
    @bicycle_client_required()
    def post(self, request, bicycle_num, remote_record_id):
        status, data = validate_form(AlterBicycleDispatchInfoForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
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

class BicycleDispatchInfosView(View):
    @session_required()
    def get(self, request, bicycle_dispatch_info_id):
        try:
            record = BicycleDispatchInfo.objects.get(bicycle_dispatch_info_id=bicycle_dispatch_info_id)
        except BicycleDispatchInfo.DoesNotExist:
            return HttpResponseNotFound()
        return HttpJsonResponse(record.detail_info())

class BicycleDispatchInfoView(View):
    @session_required()
    def get(self, request):
        flag, data = validate_form(GetBicycleDispatchInfoForm, request.jsondata)
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
        if data["dispatch_status"]:
            q &= Q(dispatch_status=data["dispatch_status"])
        responses = BicycleDispatchInfo.objects.filter(q).order_by("-updated_time")
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
            if data['dispatch_status']:
                params += '&dispatch_status=%s' % data['dispatch_status']
            response['Link'] = r'<%s%s?%s>; rel="next"' % (
                get_local_host(request), request.path, params)
        return response
