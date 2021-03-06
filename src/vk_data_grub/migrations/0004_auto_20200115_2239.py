# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-01-15 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vk_data_grub', '0003_auto_20200111_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_description',
            field=models.CharField(default=None, max_length=30000, verbose_name='Описание мероприятия'),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_image',
            field=models.URLField(max_length=255, verbose_name='Ссылка на картинку встречи'),
        ),
        migrations.AlterField(
            model_name='vkgroups',
            name='group_tag',
            field=models.CharField(default='None', max_length=15, verbose_name='Тэг группы, нужен для парсера'),
        ),
    ]
