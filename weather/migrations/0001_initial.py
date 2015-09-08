# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityInfo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('area_id', models.CharField(max_length=10)),
                ('name_en', models.CharField(max_length=20)),
                ('name_cn', models.CharField(max_length=20)),
                ('district_en', models.CharField(max_length=20)),
                ('district_cn', models.CharField(max_length=20)),
                ('prov_en', models.CharField(max_length=20)),
                ('prov_cn', models.CharField(max_length=20)),
            ],
        ),
    ]
