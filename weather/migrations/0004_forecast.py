# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20150802_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('last_update', models.DateTimeField(verbose_name='最后更新时间')),
                ('forecast_date', models.DateTimeField(verbose_name='天气预报时间')),
                ('weather_phe_day', models.IntegerField(verbose_name='白天气象编号')),
                ('weather_phe_night', models.IntegerField(verbose_name='夜晚气象编号')),
                ('temperature_day', models.FloatField(verbose_name='白天气温')),
                ('temperature_night', models.FloatField(verbose_name='夜晚气温')),
                ('wind_direct_day', models.IntegerField(verbose_name='白天风向编号')),
                ('wind_direct_night', models.IntegerField(verbose_name='夜晚风向编号')),
                ('wind_level_day', models.IntegerField(verbose_name='白天风力编号')),
                ('wind_level_night', models.IntegerField(verbose_name='夜晚风力编号')),
                ('sunraise', models.TimeField(verbose_name='日出时间')),
                ('sumset', models.TimeField(verbose_name='日落时间')),
                ('city', models.ForeignKey(to='weather.CityInfo')),
            ],
        ),
    ]
