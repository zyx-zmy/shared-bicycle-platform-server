from django.db import models
from utils.helper import unique_uuid
from utils.datetime_utils import dtt, ttd
# Create your models here.

class Company(models.Model):
	# 公司id
	company_id = models.CharField(max_length=64, primary_key=True, default=unique_uuid)
	# 公司名称
	company_name = models.CharField(max_length=125, null=True)
	# 公司地址
	company_address = models.CharField(max_length=125, null=True)
	# 公司法人
	legal_person = models.CharField(max_length=32, null=True)
	# 企业联系人
	contacts = models.CharField(max_length=32, null=True)
	# 企业联系人手机号
	contacts_phone_num = models.CharField(max_length=64, null=True)
	# 营业执照代码
	business_license = models.CharField(max_length=64, null=True)
	# 营业执照照片
	business_license_image = models.CharField(max_length=255, null=True)
	# client_id
	client_id = models.CharField(max_length=64, default=unique_uuid)
	# client_secret
	client_secret = models.CharField(max_length=64, default=unique_uuid)
	# 创建时间
	created_time = models.DateTimeField(auto_now_add=True)
	# 更新时间
	updated_time = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'company'

	def detail_info(self):
		return {
			"company_id": self.company_id,
			"company_name": self.company_name,
			"company_address": self.company_address,
			"legal_person": self.legal_person,
			"contacts": self.contacts,
			"contacts_phone_num": self.contacts_phone_num,
			"business_license": self.business_license,
			"business_license_image": self.business_license_image,
			"client_id": self.client_id,
			"client_secret": self.client_secret,
			"created_time": dtt(self.created_time),
		}