from Webscraper import CustomChrome
from pushbullet import Pushbullet
import json
from pathlib import Path
import os

if __name__ == '__main__':

    ip_info = {}       
    path_to_chrome = '/usr/bin/chromedriver' if os.name == 'posix' else None
    with CustomChrome(incognito=False, path_to_chrome=path_to_chrome, headless=True, disable_gpu=True) as web_scraper_with_context_manager:
        web_scraper_with_context_manager.browser.get('https://www.ipchicken.com')
        web_scraper_with_context_manager.wait_until_css_element_object_found('font[color="#0000FF"]')
        ip_elem = web_scraper_with_context_manager.browser.find_element_by_css_selector('font[color="#0000FF"]')
        raw_text = ip_elem.text
        ip_address = raw_text.split('\n')[0]
        ip_info['ip_address'] = ip_address
        raw_advanced_info_info = web_scraper_with_context_manager.browser.find_elements_by_css_selector('font[size="2"]')
        ip_info['name'] = raw_advanced_info_info[1].text.split(': ')[1]
        ip_info['port'] = raw_advanced_info_info[2].text.split(': ')[1]
        ip_info['browser'] = raw_advanced_info_info[3].text.split(': ')[1]
    
    with open(Path.cwd().joinpath('EnvironVars/api_key.json'), 'r') as api:
        api_key = json.loads(api.read())
    if api_key['IPAddress'] != ip_info['ip_address']:
        pb = Pushbullet(api_key['API'])
        push = pb.push_note(f"{api_key['HomeNetwork']}'s IP has been updated", f"This is the body {ip_info['ip_address']}")
        api_key['IPAddress'] = ip_info['ip_address']
        with open(Path.cwd().joinpath('EnvironVars/api_key.json'), 'w') as api:
            json.dump(api_key, api, indent=4)