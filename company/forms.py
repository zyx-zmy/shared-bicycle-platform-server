from django import forms

class CompanyForm(forms.Form):
	# 公司名称
	company_name = forms.CharField(max_length=255, required=False)
	# 公司地址
	company_address = forms.CharField(max_length=255, required=False)
	# 公司法人
	legal_person = forms.CharField(max_length=255, required=False)
	# 企业联系人
	contacts = forms.CharField(max_length=255, required=False)
	# 企业联系人手机号
	contacts_phone_num = forms.CharField(max_length=255, required=False)
	# 营业执照代码
	business_license = forms.CharField(max_length=255, required=False)
	# 营业执照照片
	business_license_image = forms.CharField(max_length=255, required=False)

class CompanysForm(forms.Form):
	# 公司名称
	company_name = forms.CharField(max_length=255, required=False)
	# 开始时间
	start_time = forms.CharField(max_length=255, required=False)
	# 结束时间
	end_time = forms.CharField(max_length=255, required=False)