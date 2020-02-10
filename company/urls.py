from django.urls import path

from company.views import CompanyView, CompanysView

urlpatterns = [
	path('admin/beian/companys', CompanyView.as_view()),
	path('admin/beian/companys/<str:company_id>', CompanysView.as_view()),
]

