# import hashlib
#
# import requests
#
# from .conf import PARKING_PASSPORT_CLIENT_ID, PARKING_PASSPORT_CLIENT_SECRET
#
#
# class OperationSessionRequest(object):
#     def __init__(self, request, **kwargs):
#         self.cookies = request.COOKIES
#
#     def get(self, url, params=None, timeout=5):
#         return requests.get(
#             url=url,
#             params=params,
#             cookies=self.cookies,
#             timeout=timeout)
#
#
# class OperationAppRequest(object):
#     def __init__(self, **kwargs):
#         pass
#
#     @property
#     def headers(self):
#         if not getattr(self, '_headers', None):
#             self._headers = {
#                 'X-CLIENT-ID': PARKING_PASSPORT_CLIENT_ID,
#                 'X-CLIENT-MD5': md5_hex_digest(
#                     '%s%s' % (
#                         PARKING_PASSPORT_CLIENT_ID,
#                         PARKING_PASSPORT_CLIENT_SECRET),
#                 )
#             }
#         return self._headers
#
#     def get(self, url, params=None, timeout=5):
#         return requests.get(
#             url=url,
#             params=params,
#             headers=self.headers,
#             timeout=timeout)
#
#
# def md5_hex_digest(value, encoding="raw_unicode_escape"):
#     h = hashlib.md5(value.encode(encoding))
#     return h.hexdigest()
#
#
# Operation_app_req = OperationAppRequest()
