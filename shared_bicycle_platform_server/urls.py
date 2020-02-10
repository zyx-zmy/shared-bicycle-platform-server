"""shared_bicycle_platform_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('bicycle_dispatch_info.urls')),
    path('', include('bicycle_driver_record.urls')),
    path('', include('bicycle_driving_range.urls')),
    path('', include('bicycle_event.urls')),
    path('', include('bicycle_order.urls')),
    path('', include('bicycle.urls')),
]
