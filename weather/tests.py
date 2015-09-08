from django.test import TestCase
from weather.models import *


# Create your tests here.
class TestWeather(TestCase):
    def setUp(self):
        from weather.api_config import query_by_areaid
        self.city = CityInfo(areaid='101010100',
                             nameen='beijing', namecn='北京',
                             districten='beijing', districtcn='北京',
                             proven='beijing', provcn='北京',
                             nationen='china', nationcn='中国')
        self.city.save()
        self.qstr = query_by_areaid(self.city.areaid)

    def test_city_update_forecast(self):
        from weather.models import update_forecast
        import json
        update_forecast(self.city, json.loads(self.qstr))
        forecasts = Forecast.objects.filter(city=self.city)
        for forecast in forecasts:
            print(forecast.forecast_date, ',', forecast.cast_time, ',', forecast.last_update, ',',
                  forecast.weather_desc(),
                  forecast.sunraise, forecast.sunset, forecast.temperature_day, forecast.temperature_night)

    def test_views(self):
        from django.test import Client
        c = Client()
        resp = c.get('/')
        self.assertEqual(resp.status_code, 200)
        resp = c.get('/101010100')
        self.assertEqual(resp.status_code, 200)
        resp = c.get('/10101010')
        self.assertEqual(resp.status_code, 404)
        resp = c.get('/filtercity/北')
        self.assertEqual(resp.status_code, 200)

    def test_update_all_city(self):
        from weather.models import update_all_city
        print('update_all_city',CityInfo.objects.all())
        update_all_city()
        forecasts = Forecast.objects.filter(city=self.city)
        for forecast in forecasts:
            print(forecast.forecast_date, ',', forecast.cast_time, ',', forecast.last_update, ',',
                  forecast.weather_desc(),
                  forecast.sunraise, forecast.sunset, forecast.temperature_day, forecast.temperature_night)

