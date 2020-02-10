from django.db import models

# Create your models here.
from utils.datetime_utils import dtt


class User(models.Model):
    # 用户id(与三方用户id一致)
    user_id = models.CharField(primary_key=True, max_length=100)
    company = models.ForeignKey('company.Company', on_delete=models.SET_NULL, null=True)
    # 注册时间
    registration_time = models.DateTimeField()
    # 信用积分
    credit_score = models.IntegerField()
    # 信用描述
    credit_des = models.CharField(max_length=500)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'

    def detail_info(self):
        return {
            'user_id': self.user_id,
            'company_id': self.company.company_id,
            'company_name': self.company.company_name,
            'registration_time': self.registration_time,
            'credit_score': self.credit_score,
            'credit_des': self.credit_des,
            'created_time': dtt(self.created_time),
            'updated_time': dtt(self.updated_time),
        }