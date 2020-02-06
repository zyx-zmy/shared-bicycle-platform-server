from django.urls import path, re_path

from user.views import AddUsers, AlterUsers

urlpatterns = [
    path('client/users', AddUsers.as_view()),
    path('client/users/<str:user_num>', AlterUsers.as_view()),
]

