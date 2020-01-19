import datetime
import vk
import json
import re

class GetDataVk:
    def  __init__(self, token=None, type_page=None):
        if type_page == 'wall':
            self.api_v = '5.3'
        elif type_page == 'group':
            self.api_v = '5.53'
        else:
            self.api_v = '5.53'

        if token:
            self.auth_token = token
        else:
            raise Exception('ERROR: need token')

    def _api(self):
        api_version = self.api_v
        session = vk.Session(access_token={self.auth_token})
        return vk.API(session, v=api_version, lang='ru', timeout=10)

    def get_events_domains_by_grdomain(self, grid, pageid):
        '''получаею id эвентов в вк из страницы группы, обычно это афиша https://vk.com/rockbus_rzn?w=page-71983141_47187398
        тут я беру форматированные строки в формате [event123|Тур в вальхалу] и получаю то что слева, пакую это в список.'''
        page_info = self._api().pages.get(owner_id=grid, page_id=pageid)
        page_info = json.dumps(page_info)
        page_info = json.loads(page_info)
        data_events = page_info['source']
        events_arr = re.findall(r'\[(.*?)\]', data_events)
        
        domains_arr = []
        for item in events_arr:
            domain = item.split('|')[0].split('/')[3]
            domains_arr.append(domain)

        return domains_arr
        
    def get_events_domains_by_grid(self, grid):
        '''Тоже самое что и метод выше, только из поля description'''
        events = self._api().groups.getById(group_ids=grid, fields="description")
        data = json.dumps(events[0])
        data_js = json.loads(data)
        data_events = data_js['description']
        future_events_list = re.findall(r'\[(.*?)\]', data_events)
    
        url_arr = []
        for event in future_events_list:
            url = event.split('|')[0]
            url_arr.append(url)

        return url_arr

    def get_event_info(self, domain):
        '''Здесь по домену группы получаю http ответ , пакую в json для дальнейшего использования'''
        info = self._api().groups.getById(group_ids=domain, fields="description,start_date")
        data = json.dumps(info[0])
        data_js = json.loads(data)

        return data_js