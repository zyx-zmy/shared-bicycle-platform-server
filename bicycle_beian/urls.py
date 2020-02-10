from django.urls import path

from bicycle_beian.views import BicycleNumbersView, BicycleBeianView, BicyclesBeianView

urlpatterns = [
	path('admin/beian/bicycles', BicycleBeianView.as_view()),
	path('admin/beian/bicycles/<str:beian_bicycle_id>', BicyclesBeianView.as_view()),
	path('admin/beian/bicycles/<str:beian_bicycle_id>/bicycle_number', BicycleNumbersView.as_view()),
]

