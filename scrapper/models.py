from datetime import datetime
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class AirReport(models.Model):
    id = models.AutoField(primary_key=True)
    air_quality =  models.CharField(verbose_name="Air Quality",  max_length=10)
    pm_2point5 = models.CharField(verbose_name="PM 2.5",  max_length=10)
    pm_10 = models.CharField(verbose_name="PM 10",  max_length=10)
    no_2 = models.CharField(verbose_name="NO2",  max_length=10)
    o_3 = models.CharField(verbose_name="O3",  max_length=10)
    co = models.CharField(verbose_name="CO",  max_length=10)
    so_2 = models.CharField(verbose_name="SO2",  max_length=10)
    temperature = models.CharField(verbose_name="Temprature",  max_length=10)
    humidity = models.CharField(verbose_name="Humidity",  max_length=10)
    wind_speed = models.CharField(verbose_name="Wind Speed",  max_length=10)
    uv = models.CharField(verbose_name="UV",  max_length=10)
    checked_on = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.checked_on
