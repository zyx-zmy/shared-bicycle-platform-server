import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.views import View

from bicycle_beian.models import BicycleBeian
from bicycle_driving_range.forms import BicycleDrivingRangeViewForm
from bicycle_driving_range.models import BicycleDrivingRange
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form
from utils.helper import HttpJsonResponse


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