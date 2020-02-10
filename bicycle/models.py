from django.db import models

# Create your models here.
from utils.datetime_utils import dtt
from utils.helper import uuid1_hex


class Bicycle(models.Model):
    bicycle_id = models.CharField(max_length=32, primary_key=True, default=uuid1_hex)
    # 车辆编号
    bicycle_num = models.CharField(max_length=100)
    # 车型编号
    bicycle_type_num = models.CharField(max_length=100)
    # # 公司id
    # company_id = models.CharField(max_length=100)
    # 公司名称
    company_name = models.CharField(max_length=100)
    # 车辆类型
    bicycle_type = models.IntegerField()
    # 定位类型 1:gps 定位 2:基站定位 3:gps 和 基站综合定位
    location_type = models.IntegerField()
    # 蓝牙 mac 地址
    bluetooth_mac = models.CharField(max_length=100)
    # 车架号
    frame_number = models.CharField(max_length=100)
    # 出厂时间(时间戳)
    production_time = models.CharField(max_length=100)
    # 初次投放时间(时间戳)
    first_put_time = models.CharField(max_length=100, null=True)
    # 最新投放时间(时间戳)
    last_put_time = models.CharField(max_length=100, null=True)
    # 最新投放位置经度，例:“124.123456”
    last_put_lon = models.CharField(max_length=100, null=True)
    # 最新投放位置纬度， 例: “24.123123”
    last_put_lat = models.CharField(max_length=100, null=True)
    # 最新投放位置信息，例:“浑南区世纪路 2 号”
    last_put_position = models.CharField(max_length=100, null=True)
    # 维修次数
    repair_count = models.IntegerField()
    # 最新维修时间(时间戳)
    last_repair_time = models.CharField(max_length=100, null=True)
    # 最新回收时间(时间戳)
    last_recovery_time = models.CharField(max_length=100, null=True)
    # 投放状态 1:未投放 2:已投放 3:维修中 4 已回收
    put_status = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bicycle'

    def detail_info(self):
        return {
            'bicycle_id': self.bicycle_id,
            'bicycle_num': self.bicycle_num,
            'bicycle_type_num': self.bicycle_type_num,
            'company_name': self.company_name,
            'bicycle_type': self.bicycle_type,
            'location_type': self.location_type,
            'bluetooth_mac': self.bluetooth_mac,
            'frame_number': self.frame_number,
            'production_time': self.production_time,
            'first_put_time': self.first_put_time,
            'last_put_time': self.last_put_time,
            'last_put_lon': self.last_put_lon,
            'last_put_lat': self.last_put_lat,
            'last_put_position': self.last_put_position,
            'repair_count': self.repair_count,
            'last_repair_time': self.last_repair_time,
            'last_recovery_time': self.last_recovery_time,
            'put_status': self.put_status,
            'created_time': dtt(self.created_time),
            'updated_time': dtt(self.updated_time)
        }
