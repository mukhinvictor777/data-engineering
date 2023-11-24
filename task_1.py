"""
Задание 1
Исследовать структуру html-файлов, чтобы произвести парсинг всех данных. В каждом файле содержится информация об одном
объекте из случайной предметной области. Полученные данные собрать и записать в json. Выполните также ряд операций с данными:
	отсортируйте значения по одному из доступных полей
	выполните фильтрацию по другому полю (запишите результат отдельно)
	для одного выбранного числового поля посчитайте статистические характеристики (сумма, мин/макс, среднее и т.д.)
	для одного текстового поля посчитайте частоту меток

"""
from bs4 import BeautifulSoup
import re
from json import dump


def parse_html(path_to_html: str) -> dict:
    with open(path_to_html, encoding='utf-8') as file:
        text = ''
        for row in file.readlines():
            text += row

    item_ = dict()
    site = BeautifulSoup(text, 'html.parser')

    chess_tour_raw = site.html.body.div.span.get_text()
    item_['type'] = chess_tour_raw.strip().split(':')[1].strip()
    item_['name'] = site.find_all('h1')[0].get_text().split(':')[1].strip()
    item_['city'] = site.find_all('p')[0].get_text().split(':')[1][:-6].strip()
    item_['date'] = site.find_all('p')[0].get_text().split(':')[2].strip()
    item_['count'] = int(site.find_all('span', attrs={'class': 'count'})[0].get_text().split(':')[1].strip())
    item_['duration'] = site.find_all('span', attrs={'class': 'year'})[0].get_text().split(':')[1].strip()
    item_['min_rank'] = int(site.find_all('span', string=re.compile('Минимальный'))[0].get_text().split(':')[1].strip())
    item_['rating'] = site.find_all('span', string=re.compile('Рейтинг:'))[0].get_text().split(':')[1].strip()
    item_['views'] = int(site.find_all('span', string=re.compile('Просмотры'))[0].get_text().split(':')[1].strip())

    return item_


items = list()
for i in range(1, 1000):
    path = f'task_1/{i}.html'
    items.append(parse_html(path))

with open('task_1_result.json', 'w', encoding='utf-8') as file:
    dump(items, file, ensure_ascii=False, indent=4)

items = sorted(items, key=lambda x: x['min_rank']*-1)
print(items[:4])
items = sorted(items, key=lambda x: x['views']*-1)
print(items[:4])

cities = dict()
for tour in items:
    if tour['city'] not in cities:
        cities[tour['city']] = 1
    else:
        cities[tour['city']] += 1


filtered_items = list()
for item in items:
    if cities[item['city']] > 19:
        filtered_items.append(item)

print(len(filtered_items))

with open('task_1_filtered.json', 'w', encoding='utf-8') as file:
    dump(filtered_items, file, ensure_ascii=False, indent=4)


sum_rank = items[0]['min_rank']
min_rank = items[0]['min_rank']
max_rank = items[0]['min_rank']

print(items[0]['min_rank'], sum)

size = len(items)
for i in range(1, size):
    sum_rank += items[i]['min_rank']
    if items[i]['min_rank'] < min_rank:
        min_rank = items[i]['min_rank']
    if items[i]['min_rank'] > max_rank:
        max_rank = items[i]['min_rank']
avr_rank = int(sum_rank / size)

print(f'\n'
      f'Сумма       {sum_rank}\n'
      f'Среднее     {avr_rank}\n'
      f'Минимум     {min_rank}\n'
      f'Максимум    {max_rank}')

cities = dict(sorted(cities.items(), key=lambda item: item[1], reverse=True))
print(cities)
