# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-10-04 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_auto_20181004_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]