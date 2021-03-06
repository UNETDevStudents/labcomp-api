# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 22:31
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_reservations', '0003_auto_20161015_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='timetable',
        ),
        migrations.AddField(
            model_name='reservation',
            name='timetable',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lab_reservations.TimeTable', verbose_name='timetable'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetable',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lab_reservations.Section', verbose_name='section'),
        ),
    ]
