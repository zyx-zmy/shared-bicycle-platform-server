from django.urls import path, re_path

from bicycle.views import AddBicycle, AlterBicycle, BicyclesView, BicycleView

urlpatterns = [
    path('client/bicycles', AddBicycle.as_view()),
    path('client/bicycles/<str:bicycle_num>', AlterBicycle.as_view()),
    path('admin/bicycles/<str:bicycle_id>', BicyclesView.as_view()),
    path('admin/bicycles', BicycleView.as_view()),
]

