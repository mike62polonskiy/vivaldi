from django.db import models

class BotInfo(models.Model):
    field_name = models.CharField(verbose_name='Тех информация', default=None, max_length=100)
    about = models.CharField(verbose_name='Информация о боте', default=None, max_length=10000)
    functions = models.CharField(verbose_name='Возможности бота', default=None, max_length=10000)
    contacts = models.CharField(verbose_name='Контакты, инфа о сотрудничестве', default=None, max_length=10000)

    def __str__(self):
        return self.field_name

    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'Инфо'

class Users(models.Model):
    user_id = models.IntegerField(verbose_name='Id телеграм пользователя', default=None)
    first_name = models.CharField(verbose_name='Имя пользователя', default=None, max_length=100)
    last_name = models.CharField(verbose_name='Фамилия пользователя', default=None, max_length=100)
    username = models.CharField(verbose_name='Никнэйм пользователя', default=None, max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
