from django.http import JsonResponse
from django.shortcuts import render
from .models import Weather
from .serializers import WeatherSerializer
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from functools import wraps
from rest_framework.views import exception_handler

# def handle_exceptions(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             error_message = str(e)
#             return Response({"status": "failed", "message": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     return wrapper

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Handle exceptions and return a 400 Bad Request response
            response = exception_handler(e, context=None)
            if response is None:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            return response
    return wrapper

class WeatherViewSet(viewsets.ViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    @handle_exceptions
    def create_city_weather(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    @handle_exceptions
    def view_city_weather(self, request, city, *args, **kwargs):

        obj = Weather.objects.filter(city=city).first()

        if not obj:
            return Response({"status": "failed", "message": "City not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = self.serializer_class(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
       
