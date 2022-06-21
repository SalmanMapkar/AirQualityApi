from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from .services import Scrapper
from .models import AirReport
from django.http import JsonResponse
from .serializer import AirReportSerializer

# Create your views here.
class ScrapeNow(APIView):
    def get(self, request, format=None):
        data = Scrapper.ScrapeData()
        return Response(data = model_to_dict(data))

class GetScrapedDataAll(APIView):
    def get(self, request, format=None):
        serialized_data = AirReportSerializer(AirReport.objects.all(), many = True)
        return Response(data = serialized_data.data)

class GetScrapedDataTop(APIView):
    def get(self, request, format=None):
        serialized_data = AirReportSerializer(AirReport.objects.all()[:5], many = True)
        return Response(data = serialized_data.data)

class GetScrapedData(APIView):
    def get(self, request, **kwargs):
        head = kwargs.get('head')
        serialized_data = AirReportSerializer(AirReport.objects.all()[:head], many = True)
        return Response(data = serialized_data.data)

