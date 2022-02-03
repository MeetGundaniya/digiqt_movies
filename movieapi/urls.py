
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from movieapi.views import API

urlpatterns = [
    path('api/<str:movie_name>', API.as_view())
]
