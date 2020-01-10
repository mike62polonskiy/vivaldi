from django.db import models

class VkGroups(models.Model):
    group_city = models.CharField(verbose_name='Город', max_length=255) 
    group_name = models.CharField(verbose_name='Название бара или клуба', max_length=255)
    group_url = models.URLField(verbose_name='Ссылка на группу в Vk', max_length=255)
    group_domain = models.CharField(verbose_name='Домен или id группы', max_length=255)
    group_tag = models.CharField(verbose_name='Тэг группы, нужен для парсера', max_length=15)

    def __str__(self):
        return self.group_name    
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Events(models.Model):
    event_name = models.CharField(verbose_name='Название мероприятия', max_length=255)
    event_date = models.DateField(verbose_name='Дата мероприятия')
    event_time = models.TimeField(verbose_name='Время начала мероприятия')
    event_place = models.CharField(verbose_name='Название площадки', max_length=255)
    event_event_url = models.URLField(verbose_name='Ссылка на встречу вконтакте')
    event_image = models.ImageField(verbose_name='Афиша мероприятия')
    event_contacts = models.CharField(verbose_name='Контакты оргов', max_length=255)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = 'Мероприятие (и/или) тур'
        verbose_name_plural = 'Мероприятия (и/или) туры'
