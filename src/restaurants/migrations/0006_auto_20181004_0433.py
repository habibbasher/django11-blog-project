# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-04 04:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20181004_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 4, 32, 59, 932193, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 4, 32, 59, 932225, tzinfo=utc)),
        ),
    ]