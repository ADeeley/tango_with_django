# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20160918_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=1),
        ),
    ]
