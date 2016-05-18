# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20160517_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
