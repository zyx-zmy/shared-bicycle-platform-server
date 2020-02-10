from django.urls import path, re_path

from bicycle_driver_record.views import AddBicycleDriverRecord
from bicycle_driving_range.views import BicycleDrivingRangeView, GetBicycleDrivingRangeView

urlpatterns = [
    path('client/bicycle_range', BicycleDrivingRangeView.as_view()),
    path('bicycle_driving_ranges', GetBicycleDrivingRangeView.as_view()),
]

