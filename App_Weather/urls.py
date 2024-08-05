from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . views import *




urlpatterns = [ 
   path('weather', WeatherViewSet.as_view({"post": "create"}), name='weather'), # weather
   path('weather/<str:city>', WeatherViewSet.as_view({"get": "retrieve_city"}), name='weather'), # weather
   
]