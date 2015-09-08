# -*-coding:utf-8-*-
from django.db import models


# Create your models here.
class CityInfo(models.Model):
    areaid = models.CharField(max_length=10)
    nameen = models.CharField(max_length=20)
    namecn = models.CharField(max_length=20)
    districten = models.CharField(max_length=20)
    districtcn = models.CharField(max_length=20)
    proven = models.CharField(max_length=20)
    provcn = models.CharField(max_length=20)
    nationen = models.CharField(max_length=20)
    nationcn = models.CharField(max_length=20)
    longitude = models.FloatField('经度', default=0)
    latitude = models.FloatField('纬度', default=0)
    elevation = models.FloatField('海拔', default=0)

    def __str__(self):
        return ','.join([self.areaid, self.namecn, self.districtcn, self.provcn])

    def read_station_info(self, forecast_dict):
        """
        read station info from open.weather.com.cn
        :param forecast_dict: json.loads(string) and string from open.weather.com.cn
        :return: None
        """
        city = forecast_dict['c']
        self.longitude = float(city['c13'])
        self.latitude = float(city['c14'])
        self.elevation = float(city['c15'])


class Forecast(models.Model):
    city = models.ForeignKey(CityInfo)
    cast_time = models.DateTimeField('预报发布时间')
    last_update = models.DateTimeField('最后查询时间', auto_now=True)
    forecast_date = models.DateField('预报日期')
    weather_phe_day = models.CharField(max_length=3, verbose_name='白天气象编号', default='99')
    weather_phe_night = models.CharField(max_length=3, verbose_name='夜晚气象编号')
    temperature_day = models.FloatField('白天气温', null=True)
    temperature_night = models.FloatField('夜晚气温')
    wind_direct_day = models.CharField(max_length=3, verbose_name='白天风向编号', default='0')
    wind_direct_night = models.CharField(max_length=3, verbose_name='夜晚风向编号')
    wind_level_day = models.CharField(max_length=3, verbose_name='白天风力编号', default='0')
    wind_level_night = models.CharField(max_length=3, verbose_name='夜晚风力编号')
    sunraise = models.TimeField('日出时间')
    sunset = models.TimeField('日落时间')

    def __str__(self):
        return '-'.join([self.city.namecn, str(self.forecast_date)])

    def weather_desc(self):
        from weather.api_config import WEATHER, WINDS_LEVEL, WINDS_DIRECT

        return {'weather_phe_day': WEATHER[self.weather_phe_day],
                'weather_phe_night': WEATHER[self.weather_phe_night],
                'wind_direct_day': WINDS_LEVEL[self.wind_direct_day],
                'wind_direct_night': WINDS_LEVEL[self.wind_direct_night],
                'wind_level_day': WINDS_DIRECT[self.wind_level_day],
                'wind_level_night': WINDS_DIRECT[self.wind_level_night]
                }

    def read_openweather(self, forecast_dict, cast_time_str, delta_date):
        """
        Read one of 'f1' parts of forecast string from open.weather.com.cn.
        :param forecast_dict: {'fa':'01'....}
        :param cast_time_str: f0, '201501011100'
        :param delta_date: forecast date - cast date
        :return: None
        """
        from django.utils.timezone import datetime, timedelta, FixedOffset
        from datetime import time
        self.cast_time = datetime(year=int(cast_time_str[0:4]), month=int(cast_time_str[4:6]),
                                  day=int(cast_time_str[6:8]), hour=int(cast_time_str[8:10]),
                                  tzinfo=FixedOffset(8 * 60))
        if forecast_dict['fa'] != "":  # check if day weather is empty
            self.weather_phe_day = forecast_dict['fa']
            self.temperature_day = float(forecast_dict['fc'])
            self.wind_direct_day = forecast_dict['fe']
            self.wind_level_day = forecast_dict['fg']
        self.weather_phe_night = forecast_dict['fb']
        self.temperature_night = float(forecast_dict['fd'])
        self.wind_direct_night = forecast_dict['ff']
        self.wind_level_night = forecast_dict['fh']
        self.forecast_date = self.cast_time.date() + timedelta(delta_date)
        sunraise = forecast_dict['fi'].split('|')[0]
        sunset = forecast_dict['fi'].split('|')[1]
        self.sunraise = time(int(sunraise[:2]), int(sunraise[3:]))
        self.sunset = time(int(sunset[:2]), int(sunset[3:]))


def update_forecast(city, qdict):
    """
    update city's forecast by qdict
    :param city:
    :param qdict:
    :return:
    """
    from django.utils.timezone import now, timedelta
    city.read_station_info(qdict)
    city.save()
    for i, adata in enumerate(qdict['f']['f1']):
        try:
            forecast = Forecast.objects.get(city=city, forecast_date=str((now() + timedelta(i)).date()))
        except Forecast.DoesNotExist:
            forecast = Forecast()
        forecast.city = city
        forecast.read_openweather(adata, qdict['f']['f0'], i)
        forecast.save()


def update_all_city():
    """
    Update all city's forecast. In order to reduce query times, query 45 cities forecasts every times from weather api.

    :return:
    """
    from time import sleep
    from weather.api_config import query_by_areaid
    import json
    import re
    query_count = 45
    lol = [CityInfo.objects.all()[i * query_count:(i + 1) * query_count] for i in
           range(int(CityInfo.objects.count() / query_count))]
    for i, city_list in enumerate(lol):
        qids = '|'.join([city.areaid for city in city_list])
        try:
            respon_str = query_by_areaid(qids)
            rs = re.sub(r'"c":({.+?})', r'\1', respon_str)
            rs = re.sub(r'"f":({.+?"f0".+?})', r'\1', rs)
            fjson = json.loads('[' + rs[1:-1] + ']')
            print(fjson)
            cs = fjson[:query_count]
            fs = fjson[query_count:]
            for c, f in zip(cs, fs):
                city = CityInfo.objects.get(areaid=c['c1'])
                update_forecast(city, {'c': c, 'f': f})
        except:
            raise Exception('forecast update failed for id:' + str(i * query_count) + '-' + str((i + 1) * query_count))

        sleep(10)
