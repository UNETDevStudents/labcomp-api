# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-06 00:04
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hourfreed',
            options={'verbose_name': 'hour freed', 'verbose_name_plural': 'hours freed'},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'reservation', 'verbose_name_plural': 'reservations'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'section', 'verbose_name_plural': 'sections'},
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'verbose_name': 'timetable', 'verbose_name_plural': 'timetables'},
        ),
        migrations.AlterField(
            model_name='hourfreed',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='hourfreed',
            name='timetable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_reservations.TimeTable', verbose_name='timetable'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='description',
            field=models.CharField(max_length=200, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_subjects.Semester', verbose_name='semester'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_subjects.Subject', verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='timetable',
            field=models.ManyToManyField(to='lab_reservations.TimeTable', verbose_name='timetable'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='type',
            field=models.IntegerField(choices=[[1, 'Partial'], [2, 'Quiz'], [3, 'Preparaduria'], [4, 'Conference'], [5, 'Review'], [6, 'Recuperative class'], [7, 'Other']], verbose_name='type of reservation'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
        migrations.AlterField(
            model_name='section',
            name='code',
            field=models.CharField(max_length=20, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='section',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_subjects.Semester', verbose_name='semester'),
        ),
        migrations.AlterField(
            model_name='section',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_subjects.Subject', verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='section',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
        migrations.AlterField(
            model_name='statusreservationhistoric',
            name='end_date',
            field=models.DateTimeField(verbose_name='end date'),
        ),
        migrations.AlterField(
            model_name='statusreservationhistoric',
            name='reservation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_reservations.Reservation', verbose_name='reservation'),
        ),
        migrations.AlterField(
            model_name='statusreservationhistoric',
            name='start_date',
            field=models.DateTimeField(verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='statusreservationhistoric',
            name='status',
            field=models.IntegerField(choices=[[1, 'Approved'], [2, 'Pending'], [3, 'Rejected'], [4, 'Canceled']], verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='block',
            field=models.IntegerField(choices=[[1, '7:00'], [2, '8:00'], [3, '9:00'], [4, '10:00'], [5, '11:00'], [6, '12:00'], [7, '13:00'], [8, '14:00'], [9, '15:00'], [10, '16:00'], [11, '17:00'], [12, '18:00'], [13, '19:00'], [14, '20:00'], [15, '21:00'], [16, '22:00']], verbose_name='block'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.IntegerField(choices=[[1, 'Lunes'], [2, 'Martes'], [3, 'Miércoles'], [4, 'Jueves'], [5, 'Viernes'], [6, 'Sábado'], [7, 'Domingo']], verbose_name='day'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_rooms.Room', verbose_name='room'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_reservations.Section', verbose_name='section'),
        ),
    ]
