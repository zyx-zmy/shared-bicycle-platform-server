from django.db import models

# Create your models here.
from utils.datetime_utils import dtt


class BicycleOrder(models.Model):
    bicycle_order_id = models.CharField(max_length=100, primary_key=True)

    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL, null=True)
    # 单车编号
    bicycle_number = models.CharField(max_length=100)
    # 用户id（编号）
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    # 开始时间
    start_time = models.CharField(max_length=100)
    # 结束时间
    end_time = models.CharField(max_length=100, null=True)
    start_lon = models.CharField(max_length=100)
    start_lat = models.CharField(max_length=100)
    # 开始位置
    start_addr = models.CharField(max_length=100)
    end_lon = models.CharField(max_length=100, null=True)
    end_lat = models.CharField(max_length=100, null=True)
    # 结束位置
    end_addr = models.CharField(max_length=100, null=True)
    # 距离 米
    driving_distance = models.IntegerField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bicycle_order'

    def detail_info(self):
        return {
            'bicycle_order_id': self.bicycle_order_id,
            'company_id': self.company.company_id,
            'company_name': self.company.company_name,
            'bicycle_number': self.bicycle_number,
            'user_id': self.user_id,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'start_lon': self.start_lon,
            'start_lat': self.start_lat,
            'start_addr': self.start_addr,
            'end_lon': self.end_lon,
            'end_lat': self.end_lat,
            'end_addr': self.end_addr,
            'driving_distance': self.driving_distance,
            'created_time': dtt(self.created_time),
            'updated_time': dtt(self.updated_time),
        }