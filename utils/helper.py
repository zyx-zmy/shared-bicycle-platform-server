import hashlib
import json
import logging
import random
import string
import time
import uuid

import math

import requests
from django.core import cache
from django.core.paginator import Paginator, EmptyPage
from django.http.response import HttpResponse

# from oauth2.helper import UuTokenHelper
# from booking_server.settings import UU_PASSPORT_DOMAIN
from utils.responses import HttpJsonResponse
from math import radians, cos, sin, asin, sqrt

logger = logging.getLogger('default')


def get_current_page(results, page_num=1, page_size=10):
    page_obj = Paginator(results, page_size)
    total_page = page_obj.num_pages
    try:
        results = page_obj.page(page_num)
    except EmptyPage:
        return None, 0
    return results, total_page


def response_errors(errors, status=422):
    return HttpJsonResponse({
        "message": "Validation Failed", "errors": errors
    }, status=status)


def json_dumps(json_object):
    return json.dumps(json_object, ensure_ascii=False)


def uuid1_hex():
    return uuid.uuid1().hex


def unique_uuid():
    return uuid.uuid1().hex


def get_local_host(request):
    uri = request.build_absolute_uri()
    return uri[0:uri.find(request.path)]


def md5_hex_digest(value, encoding="raw_unicode_escape"):
    h = hashlib.md5(value.encode(encoding))
    return h.hexdigest()


def get_timestamp():
    return int(time.time() * 1000) / 1000.0


def validate_form(form_class, data):
    form = form_class(data)
    if form.is_valid():
        return True, form.cleaned_data
    errors = []
    for key, field in form.declared_fields.items():
        if field.required and key not in data:
            errors.append({"field": key, "code": "missing_field"})
        elif key in form.errors:
            errors.append({"field": key, "code": "invalid"})
    return False, errors


class HttpJsonResponse(HttpResponse):
    def __init__(self, data=None, encoder=None, *args, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        kwargs.setdefault('status', 200)
        data = json.dumps(data, cls=encoder) if data is not None else ''
        super(HttpJsonResponse, self).__init__(content=data, *args, **kwargs)


def http_response(content=None, status=200):
    return HttpJsonResponse(content, status=status)


def create_random_string(length, letters=True, digits=True, filters=['O', 'o', '0']):
    if letters and not digits:
        raw_string = string.ascii_letters
    elif not letters and digits:
        raw_string = string.digits
    else:
        raw_string = string.ascii_letters + string.digits
    return ''.join(random.sample(filter((lambda x: False if x in filters else True), raw_string), length))


def exchange_interval(seconds):
    m, _ = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return h, m


def meters_to_lonlat(meter):
    degree = meter / (2 * math.pi * 6378137.0) * 360
    return degree


# class PhoneHelper(object):
#     @classmethod
#     def get_uu_phone_num(cls, username, uu_token):
#         phone_num = cache.get('phone_num_%s' % username)
#         if phone_num:
#             return phone_num
#         _headers = {
#             'Authorization': 'token %s' % uu_token,
#             'Content-Type': 'application/json'
#         }
#         _url = '%s/oauth/2.0/token/verifying' % UU_PASSPORT_DOMAIN
#         resp = requests.get(_url, headers=_headers)
#         logger.debug('UU_PASSPORT_DOMAIN返回code:%s' % resp.status_code)
#         if not resp:
#             logger.debug('未获取到UU_PASSPORT_DOMAIN返回值')
#             return None
#         result = resp.json()
#         phone_num = result['user']['safemobile']
#         cache.set('phone_num_%s' % username, phone_num, 60 * 10)
#         logger.debug('通过uu-token获取到的手机号：%s' % phone_num)
#         return phone_num


def md5_hex_digest(value, encoding="raw_unicode_escape"):
    h = hashlib.md5(value.encode(encoding))
    return h.hexdigest()


def point_distance(ng1, lat1, lng2, lat2):
    # 经纬度转换成弧度
    lng1, lat1, lng2, lat2 = map(radians, [float(ng1), float(lat1), float(lng2), float(lat2)])
    d_lon = lng2 - lng1
    d_lat = lat2 - lat1
    a = sin(d_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    # 地球平均半径，6371km
    distance = 2 * asin(sqrt(a)) * 6371 * 1000
    # distance = round(distance / 1000, 3)
    return distance  # 单位: 米
