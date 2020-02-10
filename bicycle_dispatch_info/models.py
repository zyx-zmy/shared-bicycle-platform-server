from django.db import models

from utils.datetime_utils import dtt
from utils.helper import uuid1_hex



class BicycleDispatchInfo(models.Model):
    bicycle_dispatch_info_id = models.CharField(max_length=32, primary_key=True, default=uuid1_hex)
    # 第三方调度记录id
    remote_record_id = models.CharField(max_length=100)
    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL, null=True)
    # 单车编号
    bicycle_number = models.CharField(max_length=100)
    # 调度状态 1未完成,2已完成
    dispatch_status = models.IntegerField()
    # 调度人
    dispatcher = models.CharField(max_length=100)
    # 调度人联系电话
    dispatcher_phone = models.CharField(max_length=100)
    # 调度开始经度
    dispatch_start_lon = models.CharField(max_length=100)
    # 调度开始纬度
    dispatch_start_lat = models.CharField(max_length=100)
    # 调度结束经度
    dispatch_end_lon = models.CharField(max_length=100)
    # 调度结束纬度
    dispatch_end_lat = models.CharField(max_length=100)
    # 调度开始时间
    dispatch_start_time = models.CharField(max_length=100)
    # 调度结束时间
    dispatch_end_time = models.CharField(max_length=100)
    # 调度开始位置
    dispatch_start_addr = models.CharField(max_length=100)
    # 调度结束位置
    dispatch_end_addr = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bicycle_dispatch_info'

    def detail_info(self):
        return {
            'bicycle_dispatch_info_id': self.bicycle_dispatch_info_id,
            'remote_record_id': self.remote_record_id,
            'company_id': self.company.company_id,
            'company_name': self.company.company_name,
            'bicycle_number': self.bicycle_number,
            'dispatch_status': self.dispatch_status,
            'dispatcher': self.dispatcher,
            'dispatcher_phone': self.dispatcher_phone,
            'dispatch_start_lon': self.dispatch_start_lon,
            'dispatch_start_lat': self.dispatch_start_lat,
            'dispatch_end_lon': self.dispatch_end_lon,
            'dispatch_end_lat': self.dispatch_end_lat,
            'dispatch_start_time': self.dispatch_start_time,
            'dispatch_end_time': self.dispatch_end_time,
            'dispatch_start_addr': self.dispatch_start_addr,
            'dispatch_end_addr': self.dispatch_end_addr,
            'created_time': dtt(self.created_time),
            'updated_time': dtt(self.updated_time),
        }