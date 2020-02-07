from django.urls import path, re_path

from bicycle_dispatch_info.views import AddBicycleDispatchInfoView, AlterBicycleDispatchInfoView

urlpatterns = [
    path('client/bicycles/<str:bicycle_num>/bicycle_transfer_records',
         AddBicycleDispatchInfoView.as_view()),
    path('client/bicycles/<str:bicycle_num>/bicycle_transfer_records/<str:remote_record_id>',
         AlterBicycleDispatchInfoView.as_view()),
]

