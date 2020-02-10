from django.db import models

# Create your models here.
from utils.datetime_utils import dtt


class BicycleEvent(models.Model):
    bicycle_event_id = models.CharField(max_length=100, primary_key=True)
    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL, null=True)
    # 单车编号
    bicycle_number = models.CharField(max_length=100)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    # 单车订单编号
    bicycle_order_id = models.CharField(max_length=100)
    # 事件类型1违规停车 2超时用车 3超范围骑行
    event_type = models.IntegerField()
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)
    start_lon = models.CharField(max_length=100)
    start_lat = models.CharField(max_length=100)
    start_addr = models.CharField(max_length=100)
    end_lon = models.CharField(max_length=100)
    end_lat = models.CharField(max_length=100)
    end_addr = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'bicycle_event'


    def detail_info(self):
        return {
            'bicycle_event_id': self.bicycle_event_id,
            'company_id': self.company.company_id,
            'company_name': self.company.company_name,
            'bicycle_number': self.bicycle_number,
            'user_id': self.user_id,
            'bicycle_order_id': self.bicycle_order_id,
            'event_type': self.event_type,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'start_lon': self.start_lon,
            'start_lat': self.start_lat,
            'end_lon': self.end_lon,
            'end_lat': self.end_lat,
            'end_addr': self.end_addr,
            'created_time': dtt(self.created_time),
            'updated_time': dtt(self.updated_time)
        }