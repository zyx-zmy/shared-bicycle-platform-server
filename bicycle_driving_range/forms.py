from django import forms

class BicycleDrivingRangeViewForm(forms.Form):
    bicycle_type_num = forms.CharField(max_length=100)
    bicycle_range = forms.CharField(max_length=1000)
    range_type = forms.IntegerField()
    range_description = forms.CharField(max_length=100)
