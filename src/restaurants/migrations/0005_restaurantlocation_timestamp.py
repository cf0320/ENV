# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurantlocation_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
