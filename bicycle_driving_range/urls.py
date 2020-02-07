from django.urls import path, re_path

from bicycle_driver_record.views import AddBicycleDriverRecord
from bicycle_driving_range.views import BicycleDrivingRangeView

urlpatterns = [
    path('client/bicycle_range', BicycleDrivingRangeView.as_view()),
]

