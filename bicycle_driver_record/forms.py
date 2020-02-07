from django import forms

from utils.time_helper import ttd


class AddBicycleDriverRecordForm(forms.Form):
    bicycle_status = forms.IntegerField()
    update_time = forms.CharField(max_length=100)
    lon = forms.CharField(max_length=100)
    lat = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)
