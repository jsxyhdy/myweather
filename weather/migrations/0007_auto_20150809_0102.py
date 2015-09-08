# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_auto_20150809_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forecast',
            old_name='sumset',
            new_name='sunset',
        ),
    ]
