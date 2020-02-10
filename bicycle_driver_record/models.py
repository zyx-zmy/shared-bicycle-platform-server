from django.db import models

# Create your models here.
from utils.datetime_utils import dtt
from utils.helper import uuid1_hex


class BicycleDriverRecord(models.Model):
    bicycle_driver_record_id = models.CharField(max_length=32, primary_key=True, default=uuid1_hex)
    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL, null=True)
    # 车辆编号
    bicycle_num = models.CharField(max_length=100)
    # 车辆状态 1:停放中 2:行驶中 3:调度 中 4:被预约
    bicycle_status = models.IntegerField()
    # 状态更新时间
    update_time = models.CharField(max_length=100)
    # 车辆位置经度，例:“124.123456”
    lon = models.CharField(max_length=100)
    # 车辆位置纬度， 例: “24.123123”
    lat = models.CharField(max_length=100)
    # 位置信息，例:“浑南区世纪路 2 号”
    position = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bicycle_driver_record'

    def detail_info(self):
        return {
            'bicycle_driver_record_id': self.bicycle_driver_record_id,
            'bicycle_num': self.bicycle_num,
            'bicycle_status': self.bicycle_status,
            'update_time': self.update_time,
            'lon': self.lon,
            'lat': self.lat,
            'position': self.position,
            'created_time': dtt(self.created_time),
            'updated_time': dtt(self.updated_time),
        }