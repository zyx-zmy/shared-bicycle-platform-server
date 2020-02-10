from django.db import models

# Create your models here.
from utils.datetime_utils import dtt
from utils.helper import uuid1_hex


class BicycleDrivingRange(models.Model):
    bicycle_driving_range_id = models.CharField(primary_key=True, max_length=32, default=uuid1_hex)
    # 企业id
    company_id = models.CharField(max_length=100)
    # 企业名称
    company_name = models.CharField(max_length=100)
    # 车型编号
    bicycle_type_number = models.CharField(max_length=100)
    # 行驶范围
    driving_range = models.CharField(max_length=1000)
    # 行驶范围限制 1允许行驶区域 2允许停放区域 3禁止停放区域
    driving_range_limit = models.IntegerField()
    # 行驶范围描述
    driving_range_des = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bicycle_driving_range'

    def detail_info(self):
        return {
            'bicycle_driving_range_id': self.bicycle_driving_range_id,
            'company_id': self.company_id,
            'company_name': self.company_name,
            'bicycle_type_number': self.bicycle_type_number,
            'driving_range': self.driving_range,
            'driving_range_limit': self.driving_range_limit,
            'driving_range_des': self.driving_range_des,
            'created_time': dtt(self.created_time),
            'updated_time': dtt(self.updated_time)
        }
