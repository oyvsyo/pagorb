# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20160518_1415'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
