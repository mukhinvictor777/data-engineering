"""
Задание 3
Считайте массив объектов в формате json. Агрегируйте информацию по каждому товару, получив следующую информацию:
средняя цена, максимальная цена, минимальная цена. Сохранить полученную информацию
"""

from json import load, dump
import msgpack
import os


with open('./3/products_67.json') as file:
    data = load(file)

fruits = dict()

for fruit in data:
    if fruit['name'] in fruits:
        fruits[fruit['name']].append(fruit['price'])
    else:
        fruits[fruit['name']] = list()
        fruits[fruit['name']].append(fruit['price'])

result = list()
for fruit, prices in fruits.items():
    sum_price = 0
    max_price = prices[0]
    min_price = prices[0]
    size = len(prices)
    for price in prices:
        sum_price += price
        max_price = max(max_price, price)
        min_price = min(min_price, price)
    result.append({
        'name': fruit,
        'max': max_price,
        'min': min_price,
        'avr': round(sum_price / size, 2)
    })

with open('task_3_result.json', 'w') as file:
    dump(result, file, ensure_ascii=False, indent=4)

with open('task_3_result.msgpack', 'wb') as file:
    file.write(msgpack.dumps(result))

print(f'json = {os.path.getsize('task_3_result.json')}')
print(f'msgpack = {os.path.getsize('task_3_result.msgpack')}')
