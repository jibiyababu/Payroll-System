# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-29 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0003_auto_20180427_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='month_year',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
