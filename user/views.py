import json
from django.http import JsonResponse, HttpResponseNotFound
from django.views import View
from user.forms import AddUsersForm, AlterUsersForm
from user.models import User
from utils.form_helper import verify_form


class AddUsers(View):

    def post(self, request):
        str = request.body.decode()
        data_dict = json.loads(str)
        data, status = verify_form(AddUsersForm, data_dict)
        if not status:
            return JsonResponse(
                status=204,
                data=data
            )
        user_data = {}
        user_data['user_id'] = data['user_num']
        user_data['company_id'] = 'company_id'
        user_data['company_name'] = 'company_name'
        user_data['registration_time'] = data['register_time']
        user_data['credit_score'] = data['credit_score']
        user_data['credit_des'] = data['credit_description']
        User.objects.create(**user_data)
        return JsonResponse(status=204, data={})


class AlterUsers(View):

    def post(self, request, user_num):
        str = request.body.decode()
        data_dict = json.loads(str)
        data, status = verify_form(AlterUsersForm, data_dict)
        if not status:
            return JsonResponse(
                status=204,
                data=data
            )
        try:
            user = User.objects.get(user_id=user_num)
        except User.DoesNotExist:
            return HttpResponseNotFound()
        user.credit_score = data['credit_score']
        user.credit_des = data['credit_description']
        user.save()
        return JsonResponse(status=204, data={})