"""
Задание 4
Считайте данные в формате pkl о товарах. Также считайте данные из файла формата json о новых ценах для каждого товара:
{
    name: "Apple",
    method: "add"|"sub"|"percent+"|"percent-",
    param: 4|0.01
}
Обновите цены для товаров в зависимости от метода:
"add" – добавить значение param к цене;
"sub" – отнять значение param от цены;
"percent+" – поднять на param % (1% = 0.01);
"percent-" – снизить на param %.
Сохраните модифицированные данные обратно в формат pkl.
"""

import pickle
import json

with open('./4/price_info_67.json', 'r') as file:
    data = json.load(file)

