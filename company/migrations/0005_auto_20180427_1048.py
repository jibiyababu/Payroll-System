# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-27 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20180414_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date',
            field=models.CharField(choices=[('2018-01-26', 'Jan'), ('2018-02-14', 'Feb 14, 2018'), ('2018-03-02', 'Mar 2, 2018'), ('2018-03-25', 'Mar 25, 2018'), ('2018-03-29', 'Mar 29, 2018'), ('2018-03-30', 'Mar 30, 2018'), ('2018-03-30', 'Apr 30, 2018'), ('2018-06-16', 'Jun 16, 2018'), ('2018-08-15', 'Aug 15, 2018'), ('2018-08-22', 'Aug 22, 2018'), ('2018-09-03', 'Sep 3, 2018'), ('2018-09-13', 'Sep 13, 2018'), ('2018-09-21', 'Sep 21, 2018'), ('2018-09-21', 'Sep 21, 2018'), ('2018-10-19', 'Oct 19, 2018'), ('2018-11-07', 'Nov 7, 2018'), ('2018-11-21', 'Nov 21, 2018'), ('2018-11-23', 'Nov 23, 2018'), ('2018-12-26', 'Dec 25, 2018'), ('2018-01-01', 'Jan 1, 2018'), ('2018-01-14', 'Jan 14, 2018')], max_length=200),
        ),
        migrations.AlterField(
            model_name='work_type',
            name='worktype',
            field=models.CharField(choices=[('SH', 'Saturday Halfday'), ('SW', 'Saturday Working'), ('SSH', 'Saturday-Sunday Holiday')], max_length=200),
        ),
    ]
