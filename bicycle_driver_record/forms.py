from django import forms



class AddBicycleDriverRecordForm(forms.Form):
    bicycle_status = forms.IntegerField()
    update_time = forms.CharField(max_length=100)
    lon = forms.CharField(max_length=100)
    lat = forms.CharField(max_length=100)
    position = forms.CharField(max_length=100)


class BicycleDriverForm(forms.Form):
    # 公司id
    company_id = forms.CharField(max_length=255, required=False)
    # 车辆编号
    bicycle_num = forms.CharField(max_length=255, required=False)
    # 车辆行驶状态
    bicycle_status = forms.IntegerField(required=False)
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