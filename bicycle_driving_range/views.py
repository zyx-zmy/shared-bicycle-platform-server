import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.views import View

from bicycle_beian.models import BicycleBeian
from bicycle_driving_range.forms import BicycleDrivingRangeViewForm, GetBicycleDrivingRangeViewForm
from bicycle_driving_range.models import BicycleDrivingRange
from company.models import Company
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.helper import HttpJsonResponse, get_local_host
from utils.decorators import session_required


class BicycleDrivingRangeView(View):
    @bicycle_client_required()
    def post(self, request):
        status, data = validate_form(BicycleDrivingRangeViewForm, request.jsondata)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        try:
            BicycleBeian.objects.get(bicycle_model_code=data['bicycle_type_num'])
        except BicycleBeian.DoesNotExist:
            return HttpResponseNotFound()
        range_dict = {}
        range_dict['company_id'] = request.company_id
        range_dict['bicycle_type_number'] = data['bicycle_type_num']
        range_dict['driving_range'] = data['bicycle_range']
        range_dict['driving_range_limit'] = data['range_type']
        range_dict['driving_range_des'] = data['range_description']
        BicycleDrivingRange.objects.update_or_create(
            bicycle_type_number=data['bicycle_type_num'],
            defaults=range_dict
        )
        return HttpResponse(status=204)

class GetBicycleDrivingRangeView(View):
    @session_required()
    def get(self, request):
        flag, data = validate_form(GetBicycleDrivingRangeViewForm, request.jsondata)
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
        responses = BicycleDrivingRange.objects.filter(q).order_by("-updated_time")
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
            response['Link'] = r'<%s%s?%s>; rel="next"' % (
                get_local_host(request), request.path, params)
        return response

