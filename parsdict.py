from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import xml.etree.ElementTree as ET

driver = webdriver.Chrome()


url = f"https://www.wowhead.com/items/weapons/type:2:18:3:16:19"
driver.get(url)

item_links = driver.find_elements(By.CSS_SELECTOR, 'a[href*="item="]')

item_ids = set()

for link in item_links:
        href = link.get_attribute('href')
        match = re.search(r'item=(\d+)', href)
        if match:
            item_id = match.group(1)
            item_ids.add(item_id)

item_ids = list(item_ids)

driver.quit()
