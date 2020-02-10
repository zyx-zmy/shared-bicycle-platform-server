from django import forms




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

class GetBicycleEventForm(forms.Form):
    # 公司id
    company_id = forms.CharField(max_length=255, required=False)
    # 车辆编号
    bicycle_number = forms.CharField(max_length=255, required=False)
    event_type = forms.IntegerField(required=False)
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



