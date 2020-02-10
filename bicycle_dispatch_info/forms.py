from django import forms



class AddBicycleDispatchInfoForm(forms.Form):
    remote_record_id = forms.CharField(max_length=100)
    transfer_status = forms.IntegerField()
    transfer_start_time = forms.CharField(max_length=100)
    transfer_end_time = forms.CharField(max_length=100, required=False)
    transfer_start_lon = forms.CharField(max_length=100)
    transfer_start_lat = forms.CharField(max_length=100)
    transfer_start_position = forms.CharField(max_length=100)
    transfer_end_lon = forms.CharField(max_length=100, required=False)
    transfer_end_lat = forms.CharField(max_length=100, required=False)
    transfer_end_position = forms.CharField(max_length=100, required=False)
    transfer_user = forms.CharField(max_length=100)
    transfer_user_tele = forms.CharField(max_length=100)


class AlterBicycleDispatchInfoForm(forms.Form):
    transfer_status = forms.IntegerField()
    transfer_start_time = forms.CharField(max_length=100)
    transfer_end_time = forms.CharField(max_length=100)
    transfer_start_lon = forms.CharField(max_length=100)
    transfer_start_lat = forms.CharField(max_length=100)
    transfer_start_position = forms.CharField(max_length=100)
    transfer_end_lon = forms.CharField(max_length=100, required=False)
    transfer_end_lat = forms.CharField(max_length=100, required=False)
    transfer_end_position = forms.CharField(max_length=100, required=False)
    transfer_user = forms.CharField(max_length=100)
    transfer_user_tele = forms.CharField(max_length=100)