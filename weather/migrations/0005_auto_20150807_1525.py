# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_forecast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='forecast_date',
            field=models.DateField(verbose_name='天气预报时间'),
        ),
    ]
