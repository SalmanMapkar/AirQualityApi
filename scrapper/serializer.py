from rest_framework import serializers
from datetime import datetime
from .models import AirReport

class AirReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirReport
        fields = ['id', 'air_quality', 'pm_2point5', 'pm_10', 'no_2', 'o_3', 'co', 'so_2', 'temperature', 'humidity', 'wind_speed', 'uv', 'checked_on']
    