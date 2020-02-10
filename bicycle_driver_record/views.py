import json

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound

# Create your views here.
from django.views import View

from bicycle.models import Bicycle
from bicycle_driver_record.forms import AddBicycleDriverRecordForm
from bicycle_driver_record.models import BicycleDriverRecord
from utils.decorators_client_bicycle import bicycle_client_required
from utils.forms import validate_form


class AddBicycleDriverRecord(View):
    @bicycle_client_required()
    def post(self, request, bicycle_num):
        status, data = validate_form(AddBicycleDriverRecordForm, request.jsondata)
        if not status:
            return JsonResponse(status=204, data=data)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        data['bicycle_num'] = bicycle_num
        data['company_id'] = request.company_id
        BicycleDriverRecord.objects.create(**data)
        return HttpResponse(status=204)