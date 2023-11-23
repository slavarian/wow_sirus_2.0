import requests
import xml.etree.ElementTree as ET
import json
import os
import sys
import django
from bs4 import BeautifulSoup
from parsdict import item_ids 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')
django.setup()

from wow_db.models import (Body_armor , Head_armor , Boots_armor ,
                           Gloves_armor , Legs_armor ,Back_armor,
                            Shoulder_armor , Wrist_armor , Belt_armor,
                            Ring , Trinket , Weapon , Amulet  )

for i in item_ids:

    url = f"https://www.wowhead.com/item={i}&xml"
    response = requests.get(url)
    xml_data = response.text

    root = ET.fromstring(xml_data)

    item_name = root.find(".//name").text.strip()
    item_level = root.find(".//level").text
    item_quality = root.find(".//quality").text
    item_subclass = root.find(".//subclass").text.strip()

    json_data = root.find(".//jsonEquip").text
    json_dict = json.loads("{" + json_data + "}")

    item_armor = json_dict.get("armor", "")
    item_str = json_dict.get("str", "")
    item_sta = json_dict.get("sta", "")
    item_agi = json_dict.get("agi", "")
    item_int = json_dict.get("int", "")
    item_hastertng = json_dict.get("hastertng", "")
    item_mastery = json_dict.get("mastrtng", "")
    item_crit = json_dict.get("critstrkrtng", "")
    item_versatility = json_dict.get("versatility", "")
    item_reqlevel = json_dict.get("reqlevel", "")
    icon_tag = root.find(".//icon")
    ins_tag = root.find(".//ins")
    if icon_tag is not None:
        icon_content = icon_tag.text.strip()
        item_img_url = f"https://wow.zamimg.com/images/wow/icons/medium/{icon_content}.jpg"

    else:
        print("Тег 'icon' не найден в XML-данных.")


    body_armor = Gloves_armor(
    title=item_name,
    item_level=item_level,
    quality=item_quality,
    armor_type=item_subclass,
    item_img=item_img_url,
    armor=int(item_armor) if item_armor else None,
    strength=int(item_str) if item_str else None,
    stamina=int(item_sta) if item_sta else None, 
    agility=int(item_agi) if item_agi else None,
    intelect=int(item_int) if item_int else None,
    haste_rating=float(item_hastertng) if item_hastertng else None,
    crit_rating=float(item_crit) if item_crit else None,
    versatility=float(item_versatility) if item_versatility else None,
    mastery=float(item_mastery) if item_mastery else None,
    required_level = int(item_reqlevel) if item_reqlevel else None,
  
            )


    if item_str:
        try:
            body_armor.strength = int(item_str)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_str}' в число.")

    if item_sta:
        try:
            body_armor.stamina = int(item_sta)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_sta}' в число.")

    if item_agi:
        try:
            body_armor.agility = int(item_agi)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_agi}' в число.")

    if item_int:
        try:
            body_armor.intelect = int(item_int)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_int}' в число.")

    if item_hastertng:
        try:
            body_armor.haste_rating = float(item_hastertng)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_hastertng}' в число.")

    if item_mastery:
        try:
            body_armor.mastery = float(item_mastery)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_mastery}' в число.")

    if item_crit:
        try:
            body_armor.crit_rating = float(item_crit)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_crit}' в число.")

    if item_versatility:
        try:
            body_armor.versatility = float(item_versatility)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_versatility}' в число.")
    if item_reqlevel:
        try:
            body_armor.required_level = float(item_reqlevel)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_reqlevel}' в число.")
    if item_armor:
        try:
            body_armor.armor = float(item_armor)
        except ValueError:
            print(f"Ошибка при попытке преобразовать '{item_armor}' в число.")
  
   
    body_armor.required_level = item_reqlevel
    item_url = url.split('&')[0]
    body_armor.item_url = item_url

    body_armor.save()

# print(item_name)
# print(f"Уровень предмета: {item_level}")
# print(f"Качество: {item_quality}")
# print(f"Подтип брони: {item_subclass}")
# print(f"Броня: {item_armor}")
# print(f"+{item_int} интеллекту")
# print(f"+{item_agi} к ловкости")
# print(f"+{item_mastery} к искустности")
# print(f"+{item_crit} к криту")
# print(f"+{item_sta} к выносливости")
# print(f"+{item_hastertng} к скорости (1.93% на {item_reqlevel} ур.)")
# print(f"+{item_versatility} к универсальности (2.07% на {item_reqlevel} ур.)")
# print(f"Требуется {item_reqlevel}-й ур.")
# print(f"ссылка на предмет: {url}")
