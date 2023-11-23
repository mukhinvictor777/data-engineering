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


def update_price(product, price_info):
    method = price_info["method"]
    if method == "sum":
        product["price"] += price_info["param"]
    elif method == "sub":
        product["price"] -= price_info["param"]
    elif method == "percent+":
        product["price"] *= (1 + price_info["param"])
    elif method == "percent-":
        product["price"] *= (1 - price_info["param"])

    product["price"] = round(product["price"], 2)


with open("4/products_0.pkl", "rb") as f:
    products = pickle.load(f)

with open('./4/price_info_67.json', 'r') as file:
    price_info = json.load(file)

price_info_dict = dict()

for item in price_info:
    price_info_dict[item["name"]] = item

for product in products:
    current_price = price_info_dict[product["name"]]
    update_price(product, current_price)

with open("products_updated.pkl", "wb") as file:
    file.write(pickle.dumps(products))
