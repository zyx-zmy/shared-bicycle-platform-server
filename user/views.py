import json

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views import View

from company.models import Company
from utils.decorators import session_required
from user.forms import AddUsersForm, AlterUsersForm, GetUserForm
from user.models import User
from utils.forms import validate_form
from utils.decorators_client_bicycle import bicycle_client_required
from utils.helper import HttpJsonResponse, get_local_host


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

class GetUserView(View):
    @session_required()
    def get(self, request):
        flag, data = validate_form(GetUserForm, request.jsondata)
        if not flag:
            return HttpJsonResponse({"message": "Validation Failed", "errors": data}, status=422)
        q = Q()
        if data["company_id"]:
            try:
                company = Company.objects.get(company_id=data["company_id"])
            except Company.DoesNotExist:
                return HttpJsonResponse([])
            q &= Q(company=company)
        if data["user_id"]:
            q &= Q(user_id=data['user_id'])
        responses = User.objects.filter(q).order_by("-updated_time")
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
            if data['user_id']:
                params += '&user_id=%s' % data['user_id']
            response['Link'] = r'<%s%s?%s>; rel="next"' % (
                get_local_host(request), request.path, params)
        return response