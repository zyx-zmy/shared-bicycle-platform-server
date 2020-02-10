from django import forms



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


class BicycleForm(forms.Form):
    # 公司id
    company_id = forms.CharField(max_length=255, required=False)
    # 车辆编号
    bicycle_num = forms.CharField(max_length=255, required=False)
    # 车型编号
    bicycle_type_num = forms.CharField(max_length=255, required=False)
    # 单车类型
    bicycle_type = forms.IntegerField(required=False)
    # 投放状态 1:未投放 2:已投放 3:维修中 4 已回收
    put_status = forms.IntegerField(required=False)
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