from django import forms

from utils.datetime_utils import ttd


class AddUsersForm(forms.Form):
    # 用户编号
    user_num = forms.CharField(max_length=32, required=True)
    # 信用积分
    credit_score = forms.IntegerField(required=True)
    # 信用描述
    credit_description = forms.CharField(max_length=32, required=True)
    # 注册时间
    register_time = forms.CharField(max_length=50, required=True)

    def clean_register_time(self):
        field = float(self.cleaned_data['register_time'])
        return ttd(field)


class AlterUsersForm(forms.Form):
    # 信用积分
    credit_score = forms.IntegerField(required=True)
    # 信用描述
    credit_description = forms.CharField(max_length=32, required=True)

class GetUserForm(forms.Form):
    # 公司id
    company_id = forms.CharField(max_length=255, required=False)
    user_id = forms.CharField(max_length=255, required=False)
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
