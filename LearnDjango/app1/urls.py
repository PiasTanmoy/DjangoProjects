from django.conf.urls import include, url
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
]