# -*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from weather.models import CityInfo, Forecast
from weather.api_config import query_by_areaid
import json


# Create your views here.
def list_city(request):
    return render(request, 'main.html')


def query_by_city(request, areaid):
    from django.utils.timezone import now
    try:
        city = CityInfo.objects.get(areaid=areaid)
        forecast_list = Forecast.objects.filter(city=city, forecast_date__gte=now().date().isoformat())
    except:
        raise
    return render(request, 'city_weather.html', {'city': city,
                                                 'forecasts': forecast_list})

def city_filter(request, begin_str):
    cities = {city.areaid: city.namecn for city in CityInfo.objects.filter(namecn__startswith=begin_str)}
    return HttpResponse(json.dumps(cities, ensure_ascii=False))
