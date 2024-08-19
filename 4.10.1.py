import requests
from bs4 import BeautifulSoup
import json

# 1 ------------------------------------------------------
url = 'http://parsinger.ru/html/mouse/3/3_11.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
result_json = {
    'name': soup.find('p', id='p_header').text,
    'price': soup.find('span', id='price').text}
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
# 3 ------------------------------------------------------