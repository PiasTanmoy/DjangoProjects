from django.conf.urls import include, url
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    url(r'^(?P<album_id>[0-9]+)$', views.details, name="details")
]
