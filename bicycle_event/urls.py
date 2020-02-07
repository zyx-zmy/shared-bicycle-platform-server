from django.urls import path, re_path

from bicycle_event.views import AddBicycleEvent, AlterBicycleEvent

urlpatterns = [
    path('client/bicycles/<str:bicycle_num>/bicycle_events',
         AddBicycleEvent.as_view()),
    path('client/bicycles/<str:bicycle_num>/bicycle_events/<str:remote_event_id>',
         AlterBicycleEvent.as_view()),
]

