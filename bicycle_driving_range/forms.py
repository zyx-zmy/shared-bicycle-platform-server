from django import forms

class BicycleDrivingRangeViewForm(forms.Form):
    bicycle_type_num = forms.CharField(max_length=100)
    bicycle_range = forms.CharField(max_length=1000)
    range_type = forms.IntegerField()
    range_description = forms.CharField(max_length=100)


class GetBicycleDrivingRangeViewForm(forms.Form):
    # 公司id
    company_id = forms.CharField(max_length=255, required=False)
    # 车辆编号
    bicycle_number = forms.CharField(max_length=255, required=False)
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
