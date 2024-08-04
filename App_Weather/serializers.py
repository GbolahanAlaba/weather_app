from rest_framework import serializers
from . models import *


class WeatherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Weather
        fields = ['id', 'city', 'date', 'temperature', 'description']
