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


def has_isbn(s):
    pass


num = 1
path = f'task_1/{num}.html'

with open(path, encoding='utf-8') as file:
    text = ''
    for row in file.readlines():
        text += row

item = dict()

site = BeautifulSoup(text, 'html.parser')
chess_tour_raw = site.html.body.div.span.get_text()
item['type'] = chess_tour_raw.strip().split(':')[1].strip()
print(item['type'])
item['name'] = site.find_all('h1')[0].get_text().split(':')[1].strip()
print(item['name'])
item['city'] = site.find_all('p')[0].get_text().split(':')[1][:-6].strip()
print(item['city'])
item['date'] = site.find_all('p')[0].get_text().split(':')[2].strip()
print(item['date'])
item['count'] = site.find_all('span', attrs={'class': 'count'})[0].get_text().split(':')[1].strip()
print(item['count'])
item['duration'] = site.find_all('span', attrs={'class': 'year'})[0].get_text().split(':')[1].strip()
print(item['duration'])
item['min_rank'] = site.find_all('span', string=re.compile('Минимальный'))[0].get_text().split(':')[1].strip()
print(item['min_rank'])
item['rating'] = site.find_all('span', string=re.compile('Рейтинг:'))[0].get_text().split(':')[1].strip()
print(item['rating'])
item['views'] = site.find_all('span', string=re.compile('Просмотры'))[0].get_text().split(':')[1].strip()
print(item['views'])

print(item)
