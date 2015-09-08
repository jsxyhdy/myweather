# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20150802_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityinfo',
            name='nationcn',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cityinfo',
            name='nationen',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
