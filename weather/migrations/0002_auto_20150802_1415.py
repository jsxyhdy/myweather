# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cityinfo',
            old_name='area_id',
            new_name='areaid',
        ),
        migrations.RenameField(
            model_name='cityinfo',
            old_name='district_cn',
            new_name='districtcn',
        ),
        migrations.RenameField(
            model_name='cityinfo',
            old_name='district_en',
            new_name='districten',
        ),
        migrations.RenameField(
            model_name='cityinfo',
            old_name='name_cn',
            new_name='namecn',
        ),
        migrations.RenameField(
            model_name='cityinfo',
            old_name='name_en',
            new_name='nameen',
        ),
        migrations.RenameField(
            model_name='cityinfo',
            old_name='prov_cn',
            new_name='provcn',
        ),
        migrations.RenameField(
            model_name='cityinfo',
            old_name='prov_en',
            new_name='proven',
        ),
    ]
