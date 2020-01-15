import vk
import json
import re

from django.conf import settings
from vk_data_grub.models import VkGroups, Events

from classes.vk_data import GetDataVk


vk_token = settings.ACCESS_TOKEN

def parse_and_save(json_data):
    json = json_data
    name = json['name']
    description = json['description']
    event_datetime = json['start_date']
    event_date = event_datetime[0]
    event_time = event_datetime[1]
    event_image = json['photo_200']
    
    event = Events.objects.get()
    event.event_name = name
    event.event_date = event_date
    event.event_time = event_time
    event.event_description = description
    event.event_place = event_place
    event.event_url = 'https://vk.com/' + domain
    event.event_image = event_image
    event.save()


def get_events_info():
    qs = VkGroups.objects.all()
    
    for item in qs:
        if item.group_afisha_id != 'None':
            type_p = 'wall'
            event_place = item.group_name
            gr_id = item.group_id
            afisha_id = item.group_afisha_id
            vk = GetDataVk(token=vk_token, type_page=type_p)
            gr_domains_arr = vk.get_events_domains_by_grdomain(gr_id, afisha_id)

            for domain in gr_domains_arr:
                result = bool(re.search(r'(album)', item))
                if result == False:
                    vk = GetDataVk(token=vk_token)
                    json = vk.get_event_info(domain)
                    parse_and_save(json)
        else:
            type_p = 'group'
            event_place = item.group_name
            gr_domain = item.group_domain
            vk = GetDataVk(token=vk_token, type_page=type_p)
            gr_domains_arr = vk.get_events_domains_by_grid(gr_domain)

            for domain in gr_domains_arr:
                result = bool(re.search(r'(album)', item))
                if result == False:
                    vk = GetDataVk(token=vk_token)
                    json = vk.get_event_info(domain)
                    parse_and_save(json)