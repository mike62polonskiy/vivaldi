# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-19 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vk_data_grub', '0009_auto_20200119_1901'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BotInfo',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
