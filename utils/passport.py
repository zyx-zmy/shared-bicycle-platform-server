# import logging
#
# import requests
# from django.core.cache import cache
# from django.conf import settings
#
# logger = logging.getLogger('default')
# PARKING_OAUTH2_DOMAIN = getattr(
#     settings, 'PARKING_OAUTH2_DOMAIN', 'https://passport-d.parkone.cn')
#
# PARKING_OAUTH2_TOKEN_CACHE = getattr(
#     settings, 'PARKING_OAUTH2_TOKEN_CACHE', ('parking_oauth2_token', 60 * 5))
# PARKING_OAUTH2_CLIENT_CACHE = getattr(
#     settings, 'PARKING_OAUTH2_CLIENT_CACHE', ('parking_oauth2_client', 60 * 5))
#
#
# def check_token(access_token):
#     user_info = cache.get(
#         '%s:%s' % (PARKING_OAUTH2_TOKEN_CACHE[0], access_token))
#     if user_info:
#         return True, user_info
#     resp = requests.get(
#         '%s/token/authorization' % PARKING_OAUTH2_DOMAIN,
#         headers={'Authorization': 'token %s' % access_token}
#     )
#     if resp.status_code == 200:
#         user_info = resp.json()
#         cache.set(
#             '%s:%s' % (PARKING_OAUTH2_TOKEN_CACHE[0], access_token),
#             user_info, PARKING_OAUTH2_TOKEN_CACHE[1])
#         return True, user_info
#     return False, None
#
#
# def check_client(client_id, client_md5):
#     client_info = cache.get(
#         '%s:%s' % (PARKING_OAUTH2_CLIENT_CACHE[0], client_md5))
#     if client_info:
#         return True, client_info
#     resp = requests.get(
#         '%s/client/authorization' % PARKING_OAUTH2_DOMAIN,
#         params={'client_id': client_id, 'sign': client_md5}
#     )
#     if resp.status_code == 200:
#         client_info = resp.json()
#         cache.set(
#             '%s:%s' % (PARKING_OAUTH2_CLIENT_CACHE[0], client_md5),
#             client_info, PARKING_OAUTH2_CLIENT_CACHE[1])
#         return True, client_info
#     return False, None
