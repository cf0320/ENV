# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_remove_restaurantlocation_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
