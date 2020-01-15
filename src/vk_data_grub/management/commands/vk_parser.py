
from django.core.management.base import BaseCommand

from utils import vk_events_info

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        vk_events_info.get_events_info()

