import json
import re
import vk

from django.conf import settings

token = settings.ACCESS_TOKEN
rock_bus_grid = settings.RZN_ROCK_BUS_GRID
rock_bus_afisha_id = settings.RZN_ROCK_BUS_AFISHA_ID

session = vk.Session(access_token={token})
api = vk.API(session, v='5.3', lang='ru', timeout=10)

def get_tours():
    tours = api.pages.get(owner_id=rock_bus_grid, page_id=rock_bus_afisha_id)
    data = json.dumps(tours)
    data_js = json.loads(data)
    data_events = data_js['source']
    fmt_data_events = data_events.replace('\n', '').replace("Прошедшие туры:", "").replace("'", "")
    events_arr = re.findall('\[(.*?)\]', fmt_data_events)
    events_arr_max_index = len(events_arr) - 1

    return events_arr

def get_shtopor_events():
    events = 

def get_svoboda_events():
