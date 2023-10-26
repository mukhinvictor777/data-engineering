"""
Считайте файл согласно вашему варианту и подсчитайте среднее арифметическое чисел по каждой строке. В результирующем файле выведите полученные данные:
average1
average2
average3
-----------
averageN
"""

import pandas as pd
import numpy as np


def count_unique_characters(row):
    characters = list(row)
    unique_characters = set(characters)
    return len(unique_characters), unique_characters


data = pd.read_csv('text_2_var_67.txt', index_col=False, header=None)
data.columns = ['numbers']
print(data.info())
print(len(data))
print(data.head())

data['unique_count'], data['unique_characters'] = zip(*data['numbers'].apply(count_unique_characters))
print(data.info())
print(data.describe())
print(data.sample(10))


data['numbers'] = data['numbers'].apply(lambda x: np.array(x.split(':')).astype(np.int32))
data.drop(columns=['unique_count', 'unique_characters'], inplace=True)
data['missing_values_count'] = data['numbers'].apply(lambda x: sum(1 for item in x if item is None or item == 0 or item == ' '))
print(data.info())
print(data['missing_values_count'].describe())
print(data.sample(10))
print(data.isna())
"""
Пропущенные значения в строках датафрейма, а также пропущенные строки отсутствуют
"""
data.drop(columns=['missing_values_count'], inplace=True)
print(data.sample(10))

data['average'] = data['numbers'].apply(lambda x: sum(x)/len(x))
data['average'] = data['average'].round(2)
print(data.sample(10))

data['average'].to_csv('text_2_var_67_result.txt', header=False, index=False)
