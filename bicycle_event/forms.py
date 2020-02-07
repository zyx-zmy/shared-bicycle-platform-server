from django import forms

from utils.time_helper import ttd


class AddBicycleEventForm(forms.Form):
    remote_event_id = forms.CharField(max_length=100)
    user_num = forms.CharField(max_length=100)
    event_type = forms.IntegerField()
    bicycle_order_id = forms.CharField(max_length=100)
    start_time = forms.CharField(max_length=100)
    end_time = forms.CharField(max_length=100)
    start_lon = forms.CharField(max_length=100)
    start_lat = forms.CharField(max_length=100)
    start_position = forms.CharField(max_length=100)
    end_lon = forms.CharField(max_length=100)
    end_lat = forms.CharField(max_length=100)
    end_position = forms.CharField(max_length=100)


class AlterBicycleEventForm(forms.Form):
    user_num = forms.CharField(max_length=100)
    event_type = forms.IntegerField()
    bicycle_order_id = forms.CharField(max_length=100)
    start_time = forms.CharField(max_length=100)
    end_time = forms.CharField(max_length=100)
    start_lon = forms.CharField(max_length=100)
    start_lat = forms.CharField(max_length=100)
    start_position = forms.CharField(max_length=100)
    end_lon = forms.CharField(max_length=100)
    end_lat = forms.CharField(max_length=100)
    end_position = forms.CharField(max_length=100)


