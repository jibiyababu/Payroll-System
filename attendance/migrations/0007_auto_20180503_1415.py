# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-03 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_attendance_lop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='lop',
            field=models.BooleanField(default=False),
        ),
    ]
