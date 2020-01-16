# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-15 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vk_data_grub', '0004_auto_20200115_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.CharField(max_length=255, verbose_name='Дата мероприятия'),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_time',
            field=models.CharField(max_length=255, verbose_name='Время начала мероприятия'),
        ),
    ]