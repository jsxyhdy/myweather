# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0009_auto_20150809_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='temperature_day',
            field=models.FloatField(verbose_name='白天气温', null=True),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='weather_phe_day',
            field=models.CharField(max_length=3, verbose_name='白天气象编号', default=''),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_direct_day',
            field=models.CharField(max_length=3, verbose_name='白天风向编号', default=''),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='wind_level_day',
            field=models.CharField(max_length=3, verbose_name='白天风力编号', default=''),
        ),
    ]
