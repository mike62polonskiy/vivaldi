from django.contrib import admin

from . import models

@admin.register(models.VkGroups)
class VkGroups(models.VkGroups):
    show_full_result_count = False

@admin.register(models.Events)
class Events(models.Events):
    show_full_result_count = False