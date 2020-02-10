# import json
# import logging
# import re
#
# from django.http.response import HttpResponseBadRequest, HttpResponseForbidden
#
#
# from utils.passport import check_token
# from utils.utils import OperationSessionRequest
#
# logger = logging.getLogger('default')
#
#
# def admin_required(
#         required=True, json_stream=True, has_version=True,
#         methods=["GET", "POST", "PUT", "DELETE", "PATCH"]):
#     def _session_required(view):
#         def __decorator(self, request, *args, **kwargs):
#             if request.method not in methods:
#                 return view(request, *args, **kwargs)
#             if not request.user.is_authenticated():
#                 return HttpResponseForbidden(json.dumps({
#                     "message": "Authorization failed"}))
#             if not request.user.is_staff and not request.user.is_superuser:
#                 return HttpResponseForbidden()
#             if not _deal_request(request):
#                 return HttpResponseBadRequest(json.dumps({
#                     "message": "Problems parsing JSON"}))
#             return view(self, request, *args, **kwargs)
#
#         return __decorator
#
#     return _session_required
#
#
# def session_required(
#         required=True, json_stream=True, has_version=True,
#         methods=["GET", "POST", "PUT", "DELETE", "PATCH"]):
#     def _session_required(view):
#         def __decorator(self, request, *args, **kwargs):
#             if request.method not in methods:
#                 return view(request, *args, **kwargs)
#             if not request.user.is_authenticated():
#                 return HttpResponseForbidden(json.dumps({
#                     "message": "Authorization failed"}))
#             if not _deal_request(request):
#                 return HttpResponseBadRequest(json.dumps({
#                     "message": "Problems parsing JSON"}))
#             return view(self, request, *args, **kwargs)
#
#         return __decorator
#
#     return _session_required
#
#
# def json_required(methods=["GET", "POST", "PUT", "DELETE", "PATCH"]):
#     def _json_required(view):
#         def __decorator(self, request, *args, **kwargs):
#             if request.method not in methods:
#                 return view(request, *args, **kwargs)
#             if not _deal_request(request):
#                 return HttpResponseBadRequest(json.dumps({
#                     "message": "Problems parsing JSON"}))
#             return view(self, request, *args, **kwargs)
#
#         return __decorator
#
#     return _json_required
#
#
# def _deal_request(request, json_stream=True):
#     if json_stream and request.method in ['PUT', 'POST', 'PATCH', 'DELETE']:
#         stream = request.body
#         if stream:
#             try:
#                 if isinstance(stream, bytes):
#                     stream = stream.decode()
#                 request.jsondata = json.loads(stream)
#             except Exception as e:
#                 if isinstance(e, ValueError):
#                     request.jsondata = {}
#                 else:
#                     return False
#         else:
#             request.jsondata = {}
#     return True
#
#
# def token_required(
#         required=True, json_stream=True, methods=[
#             "GET", "POST", "PUT", "DELETE", "PATCH"]):
#     def _token_required(view):
#         def __decorator(self, request, *args, **kwargs):
#             if request.method not in methods:
#                 return view(request, *args, **kwargs)
#             try:
#                 request.access_token = re.match(
#                     '^token (\w+)', request.META['HTTP_AUTHORIZATION']
#                 ).groups()[0]
#             except (KeyError, AttributeError):
#                 request.access_token = None
#             flag, user_info = check_token(request.access_token)
#             if required and not flag:
#                 return HttpResponseForbidden()
#             request.username = user_info['username']
#             request.client_id = request.META.get('HTTP_X_CLIENT_ID')
#             if json_stream and request.method in ['PUT', 'POST', 'PATCH']:
#                 stream = request.body
#                 request.jsondata = None
#                 if stream:
#                     try:
#                         if isinstance(stream, bytes):
#                             stream = stream.decode()
#                         request.jsondata = json.loads(stream)
#                     except ValueError:
#                         return HttpResponseBadRequest(json.dumps({
#                             "message": "Problems parsing JSON"}))
#             return view(self, request, *args, **kwargs)
#
#         return __decorator
#
#     return _token_required
#
#
# def operation_session_required(methods=["GET", "POST", "PUT", "DELETE", "PATCH"]):
#     def _session_required(view):
#         def __decorator(self, request, *args, **kwargs):
#             if request.method not in methods:
#                 return view(request, *args, **kwargs)
#             if not check_session(request):
#                 return HttpResponseForbidden()
#             return view(self, request, *args, **kwargs)
#
#         return __decorator
#
#     return _session_required
#
#
# def check_session(request):
#     '''
#     调用获取用户信息接口
#     '''
#     flag, dict_user = User(request).user_info()
#     if flag:
#         request.dict_user = dict_user
#     return flag
#
#
# class User(object):
#     def __init__(self, request):
#         self.session_id = request.COOKIES.get('operation_session')
#         self.cq = OperationSessionRequest(request)
#
#     def user_info(self):
#         try:
#             resp = self.cq.get('%s/user' % OPERATION_DOMAIN)
#         except:
#             return False, None
#         if resp.status_code == 200:
#             user = resp.json()
#             return True, user
#         return False, None
