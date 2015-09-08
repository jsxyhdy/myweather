# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_auto_20150809_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='last_update',
            field=models.DateTimeField(verbose_name='最后查询时间', auto_now=True),
        ),
    ]
