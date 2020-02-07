import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from bicycle_driving_range.forms import BicycleDrivingRangeViewForm
from bicycle_driving_range.models import BicycleDrivingRange
from utils.form_helper import verify_form


class BicycleDrivingRangeView(View):
    def post(self, request):
        str = request.body.decode()
        data_dict = json.loads(str)
        data, status = verify_form(BicycleDrivingRangeViewForm, data_dict)
        if not status:
            return JsonResponse(status=204, data=data)
        # todo 车型编号备案校验
        range_dict = {}
        range_dict['company_id'] = 'company_id'
        range_dict['company_name'] = 'company_name'
        range_dict['bicycle_type_number'] = data['bicycle_type_num']
        range_dict['driving_range'] = data['bicycle_range']
        range_dict['driving_range_limit'] = data['range_type']
        range_dict['driving_range_des'] = data['range_description']
        BicycleDrivingRange.objects.update_or_create(
            bicycle_type_number=data['bicycle_type_num'],
            defaults=range_dict
        )
        return HttpResponse(status=204)