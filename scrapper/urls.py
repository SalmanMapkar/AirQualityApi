from django.urls import path
from .views import ScrapeNow, GetScrapedData, GetScrapedDataAll, GetScrapedDataTop

urlpatterns = [
    path('get/now/', ScrapeNow.as_view()),
    path('get/all/', GetScrapedDataAll.as_view()),
    path('get/top/', GetScrapedDataTop.as_view()),
    path('get/top/<int:head>/', GetScrapedData.as_view()),

]
