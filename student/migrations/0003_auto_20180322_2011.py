# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-22 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20180320_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gratudated_and_employ',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]