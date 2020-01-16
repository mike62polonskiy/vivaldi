from django.db import models

class VkGroups(models.Model):
    group_city = models.CharField(verbose_name='Город', max_length=255) 
    group_name = models.CharField(verbose_name='Название бара или клуба', max_length=255)
    group_url = models.URLField(verbose_name='Ссылка на группу в Vk', max_length=255)
    group_domain = models.CharField(verbose_name='Домен или id группы', max_length=255)
    group_tag = models.CharField(verbose_name='Тэг группы, нужен для парсера', max_length=15, default='None')
    group_id = models.CharField(verbose_name='Id группы, в начале строки обязателен знак -', max_length=15, default='None')
    group_afisha_id = models.CharField(verbose_name='Id афиши', max_length=15, default='None')

    def __str__(self):
        return self.group_name
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Events(models.Model):
    event_domain = models.CharField(verbose_name='домен мероприятия', max_length=255, default=None)
    event_name = models.CharField(verbose_name='Название мероприятия', max_length=255)
#    event_date = models.CharField(verbose_name='Дата мероприятия', max_length=255)
#    event_time = models.CharField(verbose_name='Время начала мероприятия', max_length=255)
    event_datetime = models.DateTimeField(verbose_name='Дата и время', auto_now=False, auto_now_add=False, default=None)
    event_description = models.CharField(verbose_name='Описание мероприятия', max_length=30000, default=None)
    event_place = models.CharField(verbose_name='Название площадки', max_length=255)
    event_url = models.URLField(verbose_name='Ссылка на встречу вконтакте')
    event_image = models.URLField(verbose_name='Ссылка на картинку встречи', max_length=255)
    event_contacts = models.CharField(verbose_name='Контакты оргов', max_length=255)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = 'Мероприятие (и/или) тур'
        verbose_name_plural = 'Мероприятия (и/или) туры'
