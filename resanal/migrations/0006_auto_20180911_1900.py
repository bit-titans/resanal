# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-11 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resanal', '0005_auto_20180911_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='gpa',
            field=models.FloatField(null=True),
        ),
    ]
