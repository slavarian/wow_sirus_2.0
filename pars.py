
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')
django.setup()

import requests
from bs4 import BeautifulSoup
from wow_db.models import Body_armor
from selenium import webdriver

url = "https://www.wowhead.com/ru/items/armor/slot:5/type:3#items;100"

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

armor_data = []

for armor_row in soup.find_all('tr', class_='listview-row'):
    td_elements = armor_row.find_all('td')
    if len(td_elements) >= 11:
        try:
            title = td_elements[2].find('a', class_='q4 listview-cleartext').text
        except AttributeError:
            title = None  
        armor_rate = int(td_elements[7].text)
        type_armor_element = td_elements[10].find('a')
        type_armor = type_armor_element.text.strip() if type_armor_element else None
        try:
            equipment_level = int(td_elements[4].text) if td_elements[4].text.strip() else None
            item_level = int(td_elements[3].text) if td_elements[3].text.strip().isdigit() else None
        except ValueError:
            item_level = None
        armor_data.append({
            'title': title,
            'armor_rate': armor_rate,
            'type_armor': type_armor,
            'equipment_level': equipment_level,
            'item_level': item_level,
        })


driver.quit()

for data in armor_data:
    if data['title'] and not Body_armor.objects.filter(title=data['title']).exists():
        body_armor = Body_armor(**data)
        body_armor.save()