# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_auto_20171216_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='picture',
        ),
    ]