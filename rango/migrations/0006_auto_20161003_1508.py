# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='first_visit',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
