# import gzip
# import json
# import logging
# import re
# from io import BytesIO
#
# import requests
# from django.core.cache import cache
# from django.http.response import HttpResponseBadRequest, HttpResponseForbidden
#
# from booking_server import settings
#
# logger = logging.getLogger('default')
#
# _token_required_fashion = 'PASSPORT'
#
#
# def ht_token_required(
#         required=True, json_stream=True, has_version=True,
#         methods=["GET", "POST", "PUT", "DELETE", "PATCH"]):
#     def _ht_token_required(view):
#         def __decorator(self, request, *args, **kwargs):
#             if request.method not in methods:
#                 return view(request, *args, **kwargs)
#             request.username = None
#             try:
#                 request.access_token = re.match(
#                     '^token (\w+)', request.META['HTTP_AUTHORIZATION']).groups()[0]
#             except (KeyError, AttributeError):
#                 request.access_token = None
#             '''
#             判断鉴权方式
#             '''
#             if _token_required_fashion == 'PASSPORT':
#                 info = get_token_verifying(request.access_token)
#                 request.username = info['userid'] if info else None
#             if not request.username:
#                 return HttpResponseForbidden()
#             # 接收CLIENT_ID
#             request.client_id = request.META.get('HTTP_X_HT_CLIENT_ID')
#             _deal_request(request)
#             return view(self, request, *args, **kwargs)
#
#         return __decorator
#
#     return _ht_token_required
#
#
# def get_token_verifying(access_token):
#     if not access_token:
#         return
#     result = cache.get('oauth2_access_token_%s' % access_token)
#     if result:
#         return result
#     resp = requests.get(
#         '%s/token/verifying' % settings.HT_PASSPORT_OAUTH2_DOMAIN,
#         headers={'Authorization': 'token %s' % access_token})
#     if resp.status_code == 200:
#         result = resp.json()
#         cache.set('oauth2_access_token_%s' % access_token, result, 60 * 5)
#         return result
#
#
# def _deal_request(request, json_stream=True, has_version=True):
#     if json_stream and request.method in ['PUT', 'POST', 'PATCH']:
#         stream = request.body
#         if stream:
#             try:
#                 is_gzip = request.META.get('HTTP_CONTENT_ENCODING') == 'gzip'
#                 if is_gzip:
#                     gz = gzip.GzipFile(fileobj=BytesIO(request.body))
#                     stream = gz.read()
#                     gz.close()
#                 if isinstance(stream, bytes):
#                     stream = stream.decode()
#                     request.jsondata = json.loads(stream)
#             except:
#                 return HttpResponseBadRequest(json.dumps({
#                     "message": "Problems parsing JSON"}))
#         else:
#             request.jsondata = {}
#     if has_version:
#         try:
#             request.version = re.match(
#                 '^application/vnd.uucin.v(.+)\+json',
#                 request.META['HTTP_ACCEPT']).groups()[0]
#         except (KeyError, AttributeError):
#             request.version = None
#
#
# def token_required(view, required=True, json_stream=True,
#                    has_version=True, methods=["GET", "POST", "PUT", "DELETE", "PATCH"]):
#     def decorator(request, *args, **kwargs):
#         if request.method not in methods:
#             return view(request, *args, **kwargs)
#         request.username = None
#         try:
#             request.access_token = re.match(
#                 '^token (\w+)', request.META['HTTP_AUTHORIZATION']).groups()[0]
#
#         except (KeyError, AttributeError):
#             request.access_token = None
#         # 判断鉴权方式
#         # access_token = '2df9b064aaf614729fa6db2dd43a6ffe'
#         if _token_required_fashion == 'PASSPORT':
#             info = get_token_verifying(request.access_token)
#             # logger.debug('token_required认证结果%s' % info)
#             request.username = info['userid'] if info else None
#         if not request.username:
#             logger.debug('未找到request.username')
#             return HttpResponseForbidden()
#         # 接收CLIENT_ID
#         request.client_id = request.META.get('HTTP_X_CLIENT_ID')
#         _deal_request(request)
#         return view(request, *args, **kwargs)
#
#     return decorator
