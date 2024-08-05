from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WeatherViewSet


router = DefaultRouter()
router.register(r'weather', WeatherViewSet, basename='weather')


urlpatterns = [
    path('weather', WeatherViewSet.as_view({"post": "create"}), name='weather-create'),
    path('weather/<str:city>', WeatherViewSet.as_view({"get": "retrieve_city"}), name='weather-detail'),
]
urlpatterns += router.urls