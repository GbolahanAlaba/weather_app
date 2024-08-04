from django.db import models
import uuid
from django.utils import timezone

# Create your models here.


class Weather(models.Model):
    city = models.CharField(max_length=255, blank=True, null=True, default="")
    date = models.DateField(max_length=255, blank=True, null=True, default="")
    temperature = models.FloatField(max_length=255, blank=True, null=True, default="")
    description = models.TextField(max_length=2000, blank=True, null=True, default="")
   

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.city