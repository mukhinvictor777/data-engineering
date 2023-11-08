"""
Считайте фрагмент html из файла согласно варианту. Извлеките данные из таблицы html.
Запишите полученный csv файл.
"""

from bs4 import BeautifulSoup
import csv

items = list()

with open('text_5_var_67.txt', encoding='utf-8') as file:
    lines = file.readlines()
    html = ''
    for line in lines:
        html += line

    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr')
    rows = rows[1:]
    sum_price = 0
    average_price = 0
    for row in rows:
        cells = row.find_all('td')
        item = {
            'company': cells[0].text,
            'contact': cells[1].text,
            'country': cells[2].text,
            'price': int(cells[3].text[:-1]),
            'item': cells[4].text
        }
        items.append(item)
        sum_price += item['price']
    average_price = int(round(sum_price / len(items), 0))

    print(f'Сумма всех цен в файле: {sum_price} ₽\n'
          f'Средняя цена в файле: {average_price} ₽')
    print()
    print(items[:2])

    with open('text_5_var_67_result.txt', 'w', newline='', encoding='utf-8') as result:
        writer = csv.writer(result, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for item in items:
            writer.writerow(item.values())
    