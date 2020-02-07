from django import forms

from utils.time_helper import ttd


class AddBicycleOrderForm(forms.Form):
    remote_order_id = forms.CharField(max_length=100)
    user_num = forms.CharField(max_length=100)
    start_time = forms.CharField(max_length=100)
    end_time = forms.CharField(max_length=100, required=False)
    start_lon = forms.CharField(max_length=100)
    start_lat = forms.CharField(max_length=100)
    start_position = forms.CharField(max_length=100)
    end_lon = forms.CharField(max_length=100, required=False)
    end_lat = forms.CharField(max_length=100, required=False)
    end_position = forms.CharField(max_length=100, required=False)
    distance = forms.IntegerField(required=False)


class AlterBicycleOrderForm(forms.Form):
    user_num = forms.CharField(max_length=100)
    start_time = forms.CharField(max_length=100)
    end_time = forms.CharField(max_length=100, required=False)
    start_lon = forms.CharField(max_length=100)
    start_lat = forms.CharField(max_length=100)
    start_position = forms.CharField(max_length=100)
    end_lon = forms.CharField(max_length=100, required=False)
    end_lat = forms.CharField(max_length=100, required=False)
    end_position = forms.CharField(max_length=100, required=False)
    distance = forms.IntegerField(required=False)
