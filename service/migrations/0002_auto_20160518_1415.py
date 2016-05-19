# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('text', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=14)),
                ('date_send', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='service',
            name='enterprise',
            field=models.ForeignKey(default=0, to='service.Enterprise'),
        ),
    ]
