from django import forms

class BicycleBeianAccessNumForm(forms.Form):
	# 准入数量
	access_num = forms.IntegerField(required=True)


class BicycleBeianForm(forms.Form):
	# 公司名称
	company_name = forms.CharField(max_length=255, required=False)
	# 开始时间
	start_time = forms.CharField(max_length=255, required=False)
	# 结束时间
	end_time = forms.CharField(max_length=255, required=False)


class BicycleBeianCreateForm(forms.Form):
	# 车辆型号编码
	bicycle_model_code = forms.CharField(max_length=255, required=True)
	# 企业id
	company_id = forms.CharField(max_length=255, required=True)
	# 车辆型号名称
	bicycle_model_name = forms.CharField(max_length=255, required=True)
	# 车辆型号描述
	bicycle_model_describe = forms.CharField(max_length=255, required=True)
	# 车辆型号图片
	bicycle_model_image = forms.CharField(max_length=255, required=True)
	# 单车类型
	bicycle_type = forms.IntegerField(required=True)

class BicycleNumberGetForm(forms.Form):
	page_num = forms.IntegerField(required=False)
	page_size = forms.IntegerField(required=False)

	def clean_page_num(self):
		page_num = self.cleaned_data['page_num']
		page_num = int(page_num) if page_num else 1
		return page_num

	def clean_page_size(self):
		page_size = self.cleaned_data['page_size']
		page_size = int(page_size) if page_size else 15
		return page_size