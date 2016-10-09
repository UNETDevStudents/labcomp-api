# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-06 00:04
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteristic',
            options={'verbose_name': 'characteristic', 'verbose_name_plural': 'characteristics'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'room', 'verbose_name_plural': 'rooms'},
        ),
        migrations.AlterModelOptions(
            name='roomcharacteristic',
            options={'verbose_name': 'characteristic of the room', 'verbose_name_plural': 'characteristics of the rooms'},
        ),
        migrations.AlterModelOptions(
            name='typecharacteristic',
            options={'verbose_name': 'type of characteristic', 'verbose_name_plural': 'types of characteristics'},
        ),
        migrations.AlterModelOptions(
            name='typeinfrastructure',
            options={'verbose_name': 'type of infrastructure', 'verbose_name_plural': 'types of infrastructures'},
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='icon',
            field=models.CharField(max_length=20, verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_rooms.TypeCharacteristic', verbose_name='type of characteristic'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_rooms.TypeInfrastructure', verbose_name='type of infrastructure'),
        ),
        migrations.AlterField(
            model_name='roomcharacteristic',
            name='characteristic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_rooms.Characteristic', verbose_name='characteristic'),
        ),
        migrations.AlterField(
            model_name='roomcharacteristic',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_rooms.Room', verbose_name='room'),
        ),
        migrations.AlterField(
            model_name='roomcharacteristic',
            name='value',
            field=models.CharField(max_length=20, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='typecharacteristic',
            name='icon',
            field=models.CharField(max_length=20, verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='typecharacteristic',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='typeinfrastructure',
            name='icon',
            field=models.CharField(max_length=20, verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='typeinfrastructure',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nombre'),
        ),
    ]