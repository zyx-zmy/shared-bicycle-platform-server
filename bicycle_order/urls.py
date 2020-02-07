from django.urls import path, re_path

from bicycle_order.views import AddBicycleOrderView, AlterBicycleOrderView

urlpatterns = [
    path('client/bicycles/<str:bicycle_num>/bicycle_orders',
         AddBicycleOrderView.as_view()),
    path('client/bicycles/<str:bicycle_num>/bicycle_orders/<str:remote_order_id>',
         AlterBicycleOrderView.as_view()),
]

