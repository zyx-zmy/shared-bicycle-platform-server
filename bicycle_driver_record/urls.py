from django.urls import path, re_path

from bicycle_driver_record.views import AddBicycleDriverRecord, BicycleDriverRecordView

urlpatterns = [
	path('client/bicycles/<str:bicycle_num>/bicycle_status_records', AddBicycleDriverRecord.as_view()),
	path('admin/bicycle_status_records', BicycleDriverRecordView.as_view())
]

