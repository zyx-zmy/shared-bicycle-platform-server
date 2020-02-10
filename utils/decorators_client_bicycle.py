import base64
import json
import logging
import re
from pprint import pprint

from django.http.response import HttpResponseBadRequest, HttpResponseForbidden

from company.models import Company

logger = logging.getLogger('default')



def bicycle_client_required(
        required=True, json_stream=True, has_version=True,
        methods=["GET", "POST", "PUT", "DELETE", "PATCH"]):
    def _session_required(view):
        def __decorator(self, request, *args, **kwargs):
            if request.method not in methods:
                return view(request, *args, **kwargs)
            try:
                request.client_base64 = re.match(
                                '^Basic (.+)', request.META['HTTP_AUTHORIZATION']).groups()[0]
            except (KeyError, AttributeError):
                request.client_base64 = None
            if not request.client_base64:
                return HttpResponseForbidden(json.dumps({
                    "message": "Authorization failed"}))
            try:
                client = base64.b64decode(request.client_base64.encode()).decode()
                if '%3A' in client:
                    request.client_id = client.split('%3A')[0]
                else:
                    request.client_id = client.split(':')[0]
                company = Company.objects.get(client_id=request.client_id)
            except:
                return HttpResponseForbidden(json.dumps({
                    "message": "Authorization failed"}))
            request.company_id = company.company_id
            if not _deal_request(request):
                return HttpResponseBadRequest(json.dumps({
                    "message": "Problems parsing JSON"}))
            return view(self, request, *args, **kwargs)

        return __decorator

    return _session_required


def json_required(methods=["GET", "POST", "PUT", "DELETE", "PATCH"]):
    def _json_required(view):
        def __decorator(self, request, *args, **kwargs):
            if request.method not in methods:
                return view(request, *args, **kwargs)
            if not _deal_request(request):
                return HttpResponseBadRequest(json.dumps({
                    "message": "Problems parsing JSON"}))
            return view(self, request, *args, **kwargs)

        return __decorator

    return _json_required


def _deal_request(request, json_stream=True):
    if json_stream and request.method in ['PUT', 'POST', 'PATCH', 'DELETE']:
        stream = request.body
        if stream:
            try:
                if isinstance(stream, bytes):
                    stream = stream.decode()
                request.jsondata = json.loads(stream)
            except Exception as e:
                if isinstance(e, ValueError):
                    request.jsondata = {}
                else:
                    return False
        else:
            request.jsondata = {}
    return True


