from django.contrib import admin

from . import models

@admin.register(models.BotInfo)
class BotInfo(admin.ModelAdmin):
    show_full_result_count = False

@admin.register(models.Users)
class Users(admin.ModelAdmin):
    show_full_result_count = False