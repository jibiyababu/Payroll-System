# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-23 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20180411_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]