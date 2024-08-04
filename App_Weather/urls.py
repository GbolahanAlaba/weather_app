from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . views import *




urlpatterns = [ 
   path('weather/', WeatherViewSet.as_view({"post": "create_city_weather"}), name='weather'), # weather
   path('weather/<str:city>/', WeatherViewSet.as_view({"get": "view_city_weather"}), name='weather'), # weather
   
]