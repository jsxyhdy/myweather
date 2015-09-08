# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0005_auto_20150807_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityinfo',
            name='elevation',
            field=models.FloatField(verbose_name='海拔', default=0),
        ),
        migrations.AddField(
            model_name='cityinfo',
            name='latitude',
            field=models.FloatField(verbose_name='纬度', default=0),
        ),
        migrations.AddField(
            model_name='cityinfo',
            name='longitude',
            field=models.FloatField(verbose_name='经度', default=0),
        ),
        migrations.AddField(
            model_name='forecast',
            name='cast_time',
            field=models.DateTimeField(verbose_name='预报发布时间', default=datetime.datetime(2015, 8, 8, 16, 32, 4, 428, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forecast',
            name='forecast_date',
            field=models.DateField(verbose_name='预报日期'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='last_update',
            field=models.DateTimeField(verbose_name='最后查询时间'),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='weather_phe_day',
            field=models.CharField(verbose_name='白天气象编号', max_length=3),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='weather_phe_night',
            field=models.CharField(verbose_name='夜晚气象编号', max_length=3),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_direct_day',
            field=models.CharField(verbose_name='白天风向编号', max_length=3),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_direct_night',
            field=models.CharField(verbose_name='夜晚风向编号', max_length=3),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_level_day',
            field=models.CharField(verbose_name='白天风力编号', max_length=3),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_level_night',
            field=models.CharField(verbose_name='夜晚风力编号', max_length=3),
        ),
    ]
