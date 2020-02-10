import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound

# Create your views here.
from django.views import View

from bicycle.models import Bicycle
from bicycle_driver_record.forms import AddBicycleDriverRecordForm, BicycleDriverForm
from bicycle_driver_record.models import BicycleDriverRecord
from company.models import Company
from utils.decorators import session_required
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.helper import HttpJsonResponse, get_local_host


class AddBicycleDriverRecord(View):
    @bicycle_client_required()
    def post(self, request, bicycle_num):
        status, data = validate_form(AddBicycleDriverRecordForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        data['bicycle_num'] = bicycle_num
        data['company_id'] = request.company_id
        BicycleDriverRecord.objects.create(**data)
        return HttpResponse(status=204)

class BicycleDriverRecordView(View):
    @session_required()
    def get(self, request):
        flag, data = validate_form(BicycleDriverForm, request.jsondata)
        if not flag:
            return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
        q = Q()
        if data["company_id"]:
            try:
                company = Company.objects.get(company_id=data["company_id"])
            except Company.DoesNotExist:
                return HttpJsonResponse([])
            q &= Q(company=company)
        if data["bicycle_num"]:
            q &= Q(bicycle_num=data["bicycle_num"])
        if data["bicycle_status"]:
            q &= Q(bicycle_status=data["bicycle_status"])
        responses = BicycleDriverRecord.objects.filter(q).order_by("-updated_time")
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
            if data['bicycle_status']:
                params += '&bicycle_status=%s' % data['bicycle_status']
            response['Link'] = r'<%s%s?%s>; rel="next"' % (
                get_local_host(request), request.path, params)
        return response