from django.db import models
from utils.helper import unique_uuid
from company.models import Company
# Create your models here.

class BicycleBeian(models.Model):
	bicycle_type_choice = (
		(1,'普通单车'),
		(2,'助力车')
	)
	# id
	beian_bicycle_id = models.CharField(max_length=64, primary_key=True, default=unique_uuid)
	# 车辆型号编码
	bicycle_model_code = models.CharField(max_length=255, null=True)
	# 企业id
	company_id = models.ForeignKey('company.Company',on_delete=models.CASCADE)
	# 车辆型号名称
	bicycle_model_name = models.CharField(max_length=255, null=True)
	# 单车类型
	bicycle_type = models.IntegerField(choices=bicycle_type_choice, default=1)
	# 车辆型号描述
	bicycle_model_describe = models.CharField(max_length=255, null=True)
	# 准入数量
	access_num = models.IntegerField(default=0)
	# 车辆型号图片
	bicycle_model_image = models.CharField(max_length=255, null=True)
	# 是否含有车辆编号
	has_bicycle_number = models.BooleanField(default=False)
	# 创建时间
	created_time = models.DateTimeField(auto_now_add=True)
	# 更新时间
	updated_time = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'bicycle_beian'

	def detail_info(self):
		company = Company.objects.get(company_id=self.company_id)
		return {
			"beian_bicycle_id": self.beian_bicycle_id,
			"bicycle_model_code": self.bicycle_model_code,
			"company_name": company.company_name,
			"company_id": company_id,
			"bicycle_type": self.bicycle_type,
			"bicycle_model_name": self.bicycle_model_name,
			"bicycle_model_describe": self.bicycle_model_describe,
			"access_num": self.access_num,
			"bicycle_model_image": self.bicycle_model_image,
			"has_bicycle_number": self.has_bicycle_number,
		}

class BicycleNumber(models.Model):
	# id
	id = models.CharField(max_length=64, primary_key=True, default=unique_uuid)
	# 车辆编号
	bicycle_number = models.CharField(max_length=255, null=True)
	# 备案车辆
	beian_bicycle_id = models.CharField(max_length=255, null=True)
	# 备案企业
	company_id = models.CharField(max_length=255, null=True)
	# 创建时间
	created_time = models.DateTimeField(auto_now_add=True)
	# 更新时间
	updated_time = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'bicycle_number'

	def detail_info(self):
		return {
			"id": self.id,
			"bicycle_number": self.bicycle_number,
			"bicycle_id": self.bicycle_id,
			"company_id": self.company_id,
		}
