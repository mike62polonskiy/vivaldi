from django.db import models

class VkGroups(models.Model):
    group_city = models.CharField(verbose_name='Город', max_length=255) 
    group_name = models.CharField(verbose_name='Название бара или клуба', max_length=255)
    group_url = models.URLField(verbose_name='Ссылка на группу в Vk', max_length=255)

class Concerts(models.Model):
    concert_name = models.CharField(verbose_name='Название мероприятия', max_length=255)
    concert_date = models.DateField(verbose_name='Дата мероприятия')
    concert_time = models.TimeField(verbose_name='Время начала мероприятия')
    concert_place = models.CharField(verbose_name='Название площадки')
    concert_event_url = models.URLField(verbose_name='Ссылка на встречу вконтакте')
    concert_image = models.ImageField(verbose_name='Афиша мероприятия')
    concert_contacts = models.CharField(verbose_name='Контакты оргов')

    