# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-10 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vk_data_grub', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'verbose_name': 'Мероприятие (и/или) тур', 'verbose_name_plural': 'Мероприятия (и/или) туры'},
        ),
        migrations.AlterModelOptions(
            name='vkgroups',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
    ]
