import json
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views import View
from user.forms import AddUsersForm, AlterUsersForm
from user.models import User
from utils.forms import validate_form
from utils.decorators_client_bicycle import bicycle_client_required
from utils.helper import HttpJsonResponse


class AddUsers(View):

    @bicycle_client_required()
    def post(self, request):
        str = request.body.decode()
        data_dict = json.loads(str)
        status, data = validate_form(AddUsersForm, data_dict)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        user_data = {}
        user_data['user_id'] = data['user_num']
        user_data['company_id'] = request.company_id
        user_data['registration_time'] = data['register_time']
        user_data['credit_score'] = data['credit_score']
        user_data['credit_des'] = data['credit_description']
        User.objects.create(**user_data)
        return HttpResponse(status=204)


class AlterUsers(View):

    @bicycle_client_required()
    def post(self, request, user_num):
        str = request.body.decode()
        data_dict = json.loads(str)
        status, data = validate_form(AlterUsersForm, data_dict)
        if not status:
            return HttpJsonResponse({
                'message': 'Validate Failed',
                'errors': data}, status=422)
        try:
            user = User.objects.get(user_id=user_num)
        except User.DoesNotExist:
            return HttpResponseNotFound()
        user.credit_score = data['credit_score']
        user.credit_des = data['credit_description']
        user.save()
        return HttpResponse(status=204)