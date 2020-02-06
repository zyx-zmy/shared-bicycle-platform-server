from django import forms

from utils.time_helper import ttd


class AddBicycleForm(forms.Form):
    bicycle_num = forms.CharField(max_length=100)
    bicycle_type_num = forms.CharField(max_length=100)
    location_type = forms.IntegerField()
    bluetooth_mac = forms.CharField(max_length=100)
    frame_number = forms.CharField(max_length=100)
    production_time = forms.CharField(max_length=100)
    first_put_time = forms.CharField(max_length=100, required=False)
    last_put_time = forms.CharField(max_length=100, required=False)
    last_put_lon = forms.CharField(max_length=100, required=False)
    last_put_lat = forms.CharField(max_length=100, required=False)
    last_put_position = forms.CharField(max_length=100, required=False)
    repair_count = forms.IntegerField()
    last_repair_time = forms.CharField(max_length=100, required=False)
    last_recovery_time = forms.CharField(max_length=100, required=False)
    put_status = forms.IntegerField()

class AlterBicycleForm(forms.Form):
    bicycle_type_num = forms.CharField(max_length=100)
    location_type = forms.IntegerField()
    bluetooth_mac = forms.CharField(max_length=100)
    frame_number = forms.CharField(max_length=100)
    production_time = forms.CharField(max_length=100)
    first_put_time = forms.CharField(max_length=100, required=False)
    last_put_time = forms.CharField(max_length=100, required=False)
    last_put_lon = forms.CharField(max_length=100, required=False)
    last_put_lat = forms.CharField(max_length=100, required=False)
    last_put_position = forms.CharField(max_length=100, required=False)
    repair_count = forms.IntegerField()
    last_repair_time = forms.CharField(max_length=100, required=False)
    last_recovery_time = forms.CharField(max_length=100, required=False)
    put_status = forms.IntegerField()