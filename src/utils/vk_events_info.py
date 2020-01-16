import vk
import json
import re
import time

from django.conf import settings
from vk_data_grub.models import VkGroups, Events

from classes.vk_data import GetDataVk
from datetime import datetime


vk_token = settings.ACCESS_TOKEN

def parse_and_save(json_data, place, domain):
    json = json_data
    name = json['name']
    description = json['description']
    event_timestamp = json['start_date']
    event_datetime = datetime.fromtimestamp(event_timestamp)
    event_image = json['photo_200']
    url = 'https://vk.com/' + domain
    type_gr = json['type']

    if type_gr == 'event':       
        try:
            obj = Events.objects.get(event_domain=domain)
        except Events.DoesNotExist:
            obj = Events(event_domain=domain, event_name = name, 
                         event_datetime=event_datetime,
                         event_description=description,
                         event_place=place,
                         event_url=url,
                         event_image=event_image
                        )
            obj.save()
    else:
        print('Not a event type')


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
                result = re.search(r'(album)', domain)
                if result:
                    print('INFO: not event domain or url')
                else:
                    vk = GetDataVk(token=vk_token)
                    '''у вк ограничение на запросы, поэтому перед каждым обращением делаю sleep'''
                    time.sleep(10)
                    json = vk.get_event_info(domain)
                    parse_and_save(json, event_place, domain)
        else:
            type_p = 'group'
            event_place = item.group_name
            gr_domain = item.group_domain
            vk = GetDataVk(token=vk_token, type_page=type_p)
            gr_domains_arr = vk.get_events_domains_by_grid(gr_domain)

            for domain in gr_domains_arr:
                result = re.search(r'(album)', domain)
                if result:
                    print('INFO: not event domain or url')
                else:
                    vk = GetDataVk(token=vk_token)
                    '''у вк ограничение на запросы, поэтому перед каждым обращением делаю sleep'''
                    time.sleep(10)
                    json = vk.get_event_info(domain)
                    parse_and_save(json, event_place, domain)