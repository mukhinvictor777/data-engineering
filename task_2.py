"""
Задание 2
Исследовать структуру html-файлов, чтобы произвести парсинг всех данных. В каждом файле содержится информация об одном
или нескольких объектах из случайной предметной области. Перечень всех характеристик объекта может меняться
(у отдельного объекта могут отсутствовать некоторые характеристики). Полученные данные собрать и записать в json.
Выполните также ряд операций с данными:
	отсортируйте значения по одному из доступных полей
	выполните фильтрацию по другому полю (запишите результат отдельно)
	для одного выбранного числового поля посчитайте статистические характеристики (сумма, мин/макс, среднее и т.д.)
	для одного текстового поля посчитайте частоту меток
"""

from typing import Any
from bs4 import BeautifulSoup
import pandas as pd


def find_median(values):
    n = len(values)
    sorted_values = sorted(values)
    mid = n // 2

    if n % 2 == 0:
        # Если количество элементов четное, медиана - среднее двух центральных чисел
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        # Если количество элементов нечетное, медиана - центральное число
        return sorted_values[mid]


def parse_html(path_to_html: str) -> list[dict[str | Any, int | str | Any]]:
    with open(path_to_html, encoding='utf-8') as file:
        text = ''
        for row in file.readlines():
            text += row
    site = BeautifulSoup(text, 'html.parser')
    products = site.find_all('div', attrs={'class': 'product-item'})
    items = list()
    for product in products:
        item = dict()
        item['id'] = int(product.a['data-id'])
        item['link'] = product.find_all('a')[1]['href']
        item['img_url'] = product.find_all('img')[0]['src']
        title = product.find_all('span')[0].get_text().strip().split()
        item['diagonal'] = float(title[0][:3])
        if len(title) == 3:
            item['title'] = title[1]
        else:
            item['title'] = title[1:len(title)]
        if 'iPhone' in title:
            item['brand'] = 'Apple'
        else:
            item['brand'] = title[1]
        item['price'] = int(product.price.get_text().replace('₽', '').replace(' ', '').strip())
        item['bonus'] = int(product.strong.get_text().replace('+ начислим ', '').replace(' бонусов', '').strip())
        props = product.ul.find_all('li')
        for prop in props:
            item[prop['type']] = prop.get_text().strip()
        items.append(item)
    return items


items = list()
df = pd.DataFrame()

for i in range(1, 92):
    file_name = f'task_2/{i}.html'
    item = parse_html(file_name)
    items += item

    if isinstance(item, dict):
        item = [item]

    new_df = pd.DataFrame(item)

    if df.empty:
        df = new_df
    else:
        for col in new_df.columns:
            if col not in df.columns:
                df[col] = None

        df = pd.concat([df, new_df], ignore_index=True)


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

df = df.set_index('id')
print(len(df))
print(df.info())
df = df.sort_values(by='price', ascending=False)
print(df.head(5))
print(len(items))
items = sorted(items, key=lambda x: x['price'], reverse=True)
for i in range(5):
    print(items[i])
filtered_df = df[df['brand'].str.lower() == 'apple']
print(filtered_df.head())
print(len(filtered_df))
filtered_items = [item for item in items if item['brand'].lower() == 'apple']
print(len(filtered_items))
for i in range(5):
    print(filtered_items[i])
price_stat_df = {
        'sum':      df['price'].sum(),
        'max':      df['price'].max(),
        'min':      df['price'].min(),
        'mean':     df['price'].mean(),
        'median':   int(df['price'].median())
    }
print(price_stat_df)
price_stat_items = {
        'sum':      sum(item['price'] for item in items),
        'max':      max(item['price'] for item in items),
        'min':      min(item['price'] for item in items),
        'mean':     sum(item['price'] for item in items)/len(items),
        'median':   find_median([item['price'] for item in items])
    }
print(price_stat_items)

brand = 'Apple'
brand_count_df = {
        brand: df[df['brand'].str.lower() == brand.lower()].count().iloc[0]
}
print(brand_count_df)
brand_count_item = {
    brand: len([item for item in items if item['brand'].lower() == brand.lower()])
}
print(brand_count_item)
