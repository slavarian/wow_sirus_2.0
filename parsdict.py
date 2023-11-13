from selenium import webdriver
from selenium.webdriver.common.by import By
import re

# Укажите путь к драйверу Chrome
driver = webdriver.Chrome()


url = "https://www.wowhead.com/ru/items/armor/quality:4/slot:1/type:4#items;50-3+18"
driver.get(url)

# Используйте Selenium для извлечения данных
item_links = driver.find_elements(By.CSS_SELECTOR, 'a[href*="item="]')

# Создайте пустой список для хранения цифр
item_ids = set()

# Извлеките цифры из атрибутов href и добавьте их в множество
for link in item_links:
    href = link.get_attribute('href')
    match = re.search(r'item=(\d+)', href)
    if match:
        item_id = match.group(1)
        item_ids.add(item_id)

# Преобразуйте множество в список, если это необходимо
item_ids = list(item_ids)

# Выведите список цифр


# Закройте браузер
driver.quit()

