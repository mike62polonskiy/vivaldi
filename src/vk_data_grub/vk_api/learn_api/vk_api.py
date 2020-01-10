import vk
import json
import re

token = ''
session = vk.Session(access_token={token})
api = vk.API(session, v='5.3', lang='ru', timeout=10)
api_5_103 = vk.API(session, v='5.53', lang='ru', timeout=10)

rock_bus_grid = "-71983141"
rock_bus_afisha_id = "47187398"
shtopor_gr_domain = "rzn_liveconcerts"

def get_group_posts(group):
    posts = api.wall.get(domain=group)
    return posts

def get_tours():
    tours = api.pages.get(owner_id=rock_bus_grid, page_id=rock_bus_afisha_id)
    data = json.dumps(tours)
    data_js = json.loads(data)
    data_events = data_js['source']
    fmt_data_events = data_events.replace('\n', '').replace("Прошедшие туры:", "").replace("'", "")
    events_arr = re.findall('\[(.*?)\]', fmt_data_events)
    events_arr_max_index = len(events_arr) - 1
    del events_arr[events_arr_max_index]

    url_arr = []
    for event in events_arr:
        url = event.split('|')[0].split('/')[3]
        url_arr.append(url)

    return url_arr

def get_shtopor_events():
    events = api_5_103.groups.getById(group_ids=shtopor_gr_domain, fields="description")
    data = json.dumps(events[0])
    data_js = json.loads(data)
    data_events = data_js['description']
    fmt_data_events = data_events.replace('★', '').replace('РАСПИСАНИЕ МЕРОПРИЯТИЙ', '').replace('\n', '').replace('...', '')
    future_events = fmt_data_events[:fmt_data_events.find('ПРОШЕДШИЕ КОНЦЕРТЫ')]
    future_events_list = re.findall('\[(.*?)\]', future_events)

    url_arr = []
    for event in future_events_list:
        url = event.split('|')[0]
        url_arr.append(url)

    return url_arr

def get_event_info():
    shtopor_domains = get_shtopor_events()
    rzn_bus_domains = get_tours()
    all_domains = shtopor_domains + rzn_bus_domains

    for event in all_domains:
        

    return all_domains
    

if __name__ == "__main__":
    print(get_event_info())