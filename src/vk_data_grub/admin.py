from django.contrib import admin

from . import models

@admin.register(models.VkGroups)
class VkGroups(admin.ModelAdmin):
    show_full_result_count = False

@admin.register(models.Events)
class Events(admin.ModelAdmin):
    show_full_result_count = False