import csv
from bs4 import BeautifulSoup
import requests

# Открываем CSV файл для записи
with open('res_1.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Name', 'Description', 'Price'])  # Заголовки столбцов

    # URL первой страницы
    url = 'https://parsinger.ru/html/index1_page_1.html'
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    # Находим количество страниц
    pagen = int(soup.find('div', class_='pagen').find_all('a')[-1].text)

    # Проходим по каждой странице
    for i in range(1, pagen + 1):
        url = f'https://parsinger.ru/html/index1_page_{i}.html'
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        # Находим все товары на странице
        names = soup.find_all('a', class_='name_item')
        descriptions = soup.find_all('div', class_='description')
        prices = soup.find_all('p', class_='price')

        # Обрабатываем каждый товар
        for name, description, price in zip(names, descriptions, prices):
            name_text = name.text.strip()
            description_text = description.text.strip().replace('\n', ' ')
            
            # Проверяем наличие разделителя ':' в описании
            if ':' in description_text:
                description_text = description_text.split(':', 1)[1].strip()
            else:
                description_text = ''  # Или можно оставить описание как есть

            price_text = price.text.strip()

            # Записываем данные в CSV
            writer.writerow([name_text, description_text, price_text])