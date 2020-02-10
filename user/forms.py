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

