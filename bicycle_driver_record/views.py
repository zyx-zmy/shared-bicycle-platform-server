import json

from django.http import JsonResponse, HttpResponse, HttpResponseNotFound

# Create your views here.
from django.views import View

from bicycle.models import Bicycle
from bicycle_driver_record.forms import AddBicycleDriverRecordForm
from bicycle_driver_record.models import BicycleDriverRecord
from utils.form_helper import verify_form


class AddBicycleDriverRecord(View):

    def post(self, request, bicycle_num):
        str = request.body.decode()
        data_dict = json.loads(str)
        data, status = verify_form(AddBicycleDriverRecordForm, data_dict)
        if not status:
            return JsonResponse(status=204, data=data)
        try:
            Bicycle.objects.get(bicycle_num=bicycle_num)
        except Bicycle.DoesNotExist:
            return HttpResponseNotFound()
        data['bicycle_num'] = bicycle_num
        BicycleDriverRecord.objects.create(**data)
        return HttpResponse(status=204)