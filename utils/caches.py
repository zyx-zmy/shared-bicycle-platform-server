# # encoding:utf-8
#
# from django.conf import settings
#
# from utils import get_redis_conn
#
#
# class LockCache(object):
#     def __init__(self, specification_id):
#         self.user_conn = get_redis_conn()
#         self.specification_key = specification_id
#
#     # 规格缓存
#     def get_specification(self):
#         specification_id = self.user_conn.get(self.specification_key)
#         if specification_id:
#             return bool(specification_id.decode())  # 返回 True
#         else:
#             return None
#
#     def set_specification(self):
#         self.user_conn.set(self.specification_key, True, 3)
#         return True
#
#     def delete_specification(self):
#         self.user_conn.delete(self.specification_key)
#
#
# class CeleryTaskCache(object):
#     def __init__(self, order_id):
#         self.user_conn = get_redis_conn()
#         self.order_key = order_id
#
#     # 订单异步任务id缓存
#     def get_task_id(self):
#         task_id = self.user_conn.get(self.order_key)
#         if task_id:
#             return task_id.decode()  # 返回 task_id
#         else:
#             return None
#
#     def set_task_id(self, task_id):
#         self.user_conn.set(self.order_key, task_id, 60 * 60 * 24 * 15)  # 15天
#         return True
#
#     def delete_task_id(self):
#         self.user_conn.delete(self.order_key)
