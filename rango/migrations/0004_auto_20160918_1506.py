# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-18 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20160918_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
