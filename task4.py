"""
Задание 4
Считайте csv файл согласно вашему варианту. Структура файла имеет следующий вид по колонкам в порядке их следования:
порядковый номер, имя, фамилия, возраст, доход, номер телефона.
Необходимо выполнить следующие действия:
1)	Удалить колонку с номером телефона
2)	Рассчитайте средний доход по данным, а затем отфильтруйте те строки, доход которых меньше среднего.
3)	Также примените фильтр по колонке возраст, оставив строки со значением более
Запишите полученные результаты в новый файл csv, произведя при этом сортировку по полю номер (по возрастанию):
#заголовок для примера
#id,name,age,salary
1, Connor John, 25, 1000₽
"""

import csv

average_salary = 0
items = list()

with open('text_4_var_67.txt', newline='\n', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        item = {
            'number': int(row[0]),
            'name': row[2] + ' ' + row[1],
            'age': int(row[3]),
            'salary': int(row[4][0:-1])
        }
        average_salary += item['salary']
        items.append(item)

average_salary = round(average_salary / len(items), 2)
age = 25 + 67 % 10

filtered = list()
for item in items:
    if item['salary'] < average_salary and item['age'] > age:
        filtered.append(item)

filtered = sorted(filtered, key=lambda i: i['number'])

with open('text_4_var_67_result.txt', 'w', newline='', encoding='utf-8') as result:
    writer = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for item in filtered:
        writer.writerow(item.values())
