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

class GetBicycleDispatchInfoForm(forms.Form):
    # 公司id
    company_id = forms.CharField(max_length=255, required=False)
    # 车辆编号
    bicycle_number = forms.CharField(max_length=255, required=False)
    dispatch_status = forms.IntegerField(required=False)
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
