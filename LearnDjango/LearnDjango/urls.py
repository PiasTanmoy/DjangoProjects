from django.conf.urls import include, url
from . import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('', views.home),
    path('app1/', include('app1.urls')),
    path('admin/', admin.site.urls)
]
