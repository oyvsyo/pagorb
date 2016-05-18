# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20160517_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='description',
            field=models.CharField(default=' ', max_length=500),
            preserve_default=False,
        ),
    ]
