import vk
import json
import re

from django.conf import settings

from vk_data_grub.models import VkGroups, Events

token = settings.ACCESS_TOKEN
session = vk.Session(access_token={token})
api = vk.API(session, v='5.3', lang='ru', timeout=10)
api_5_103 = vk.API(session, v='5.53', lang='ru', timeout=10)


def _get_tours():
    qs = VkGroups.objects.filter(group_tag='rockbus_rzn')
    rock_bus_grid = qs.values('group_id')[0]['group_id']
    rock_bus_afisha_id = qs.values('group_afisha_id')[0]['group_afisha_id']

    tours = api.pages.get(owner_id=rock_bus_grid, page_id=rock_bus_afisha_id)
    data = json.dumps(tours)
    data_js = json.loads(data)
    data_events = data_js['source']
    fmt_data_events = data_events.replace('\n', '').replace("Прошедшие туры:", "").replace("'", "")
    events_arr = re.findall(r'\[(.*?)\]', fmt_data_events)
    events_arr_max_index = len(events_arr) - 1
    del events_arr[events_arr_max_index]

    url_arr = []
    for event in events_arr:
        url = event.split('|')[0].split('/')[3]
        url_arr.append(url)

    return url_arr

def _get_shtopor_events():
    qs = VkGroups.objects.filter(group_tag='shtopor')
    shtopor_gr_domain = qs.values('group_domain')[0]['group_domain'] 

    events = api_5_103.groups.getById(group_ids=shtopor_gr_domain, fields="description")
    data = json.dumps(events[0])
    data_js = json.loads(data)
    data_events = data_js['description']
    fmt_data_events = data_events.replace('★', '').replace('РАСПИСАНИЕ МЕРОПРИЯТИЙ', '').replace('\n', '').replace('...', '')
    future_events = fmt_data_events[:fmt_data_events.find('ПРОШЕДШИЕ КОНЦЕРТЫ')]
    future_events_list = re.findall(r'\[(.*?)\]', future_events)

    url_arr = []
    for event in future_events_list:
        url = event.split('|')[0]
        url_arr.append(url)

    return url_arr

#Кришна петух, он ведет группу как попало. Его поглатила водяра!!! поэтому сперва делаю выборку из ивентов имеющих встречу в вк.
def _get_krishna_events_with_club():
    qs = VkGroups.objects.filter(group_tag='svoboda')
    svoboda_gr_domain = qs.values('group_domain')[0]['group_domain']

    events = api_5_103.groups.getById(group_ids=svoboda_gr_domain, fields="description")
    data = json.dumps(events[0])
    data_js = json.loads(data)
    data_events = data_js['description'].replace('►', '')
    all_sv_events_arr = data_events.split('\n')

    events_with_club = []
    for item in all_sv_events_arr:
        result = re.search(r'(club)', item)
        if bool(result) == True:
            events_with_club.append(item)

    events_domain = []
    for event in events_with_club:
        item_with_domain = re.findall(r'\[(.*?)\]', event)[0]
        item_with_domain = item_with_domain.split('|')[0]
        events_domain.append(item_with_domain)

    return events_domain

def get_info_and_save(domains, group_tag):

    for domain in domains:
        if group_tag == 'shtopor':
            place = 'Штопор(группа rzn live concerts)'
        elif group_tag == 'rockbus_rzn':
            place = 'RockBus(не клуб, выезды по городам)'
        elif group_tag == 'svoboda':
            place = 'SVОBODA'
        
        event_info = api_5_103.groups.getById(group_ids=domain, fields="description,start_date")
        data = json.dumps(event_info[0])
        data_js = json.loads(data)
        name = data_js['name']
        description = data_js['description']
        event_datetime = data_js['start_date']
        event_date = event_datetime[0]
        event_time = event_datetime[1]
        event_image = data_js['photo_200']

        event = Events.objects.get()
        event.event_name = name
        event.event_date = event_date
        event.event_time = event_time
        event.event_description = description
        event.event_place = place
        event.event_url = 'https://vk.com/' + domain
        event.event_image = event_image
        event.save()

