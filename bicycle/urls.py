from django.urls import path, re_path

from bicycle.views import AddBicycle, AlterBicycle

urlpatterns = [
    path('client/bicycles', AddBicycle.as_view()),
    path('client/bicycles/<str:bicycle_num>', AlterBicycle.as_view()),
]

