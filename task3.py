"""
Считайте файл согласно вашему варианту. В строках имеются пропуски, обозначенные «NA» – замените их, рассчитав среднее
значение соседних чисел. Затем отфильтруйте значения на каждой строке, исключив те числа, корень квадратный из которых
будет меньше  . В результирующем файле запишите полученные данные.
"""

import pandas as pd
import numpy as np
import string
from math import sqrt


def count_unique_characters(row):
    characters = list(row)
    unique_characters = set(characters)
    return len(unique_characters), unique_characters


with open('text_3_var_67.txt', 'r') as file:
    lines = file.readlines()

matrix = list()
to_translate = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

for line in lines:
    line = line.translate(to_translate)
    nums = line.split()
    for i in range(len(nums)):
        if nums[i] == 'NA':
            nums[i] = str((float(nums[i-1])+(float(nums[i-1])) / 2))

    filtered = list()
    for item in nums:
        num = float(item)
        if sqrt(num) > 50:
            filtered.append(num)

    matrix.append(filtered)

    with open('text_3_var_67_result.txt', 'w') as result:
        for row in matrix:
            for num in row:
                result.write(str(num) + ',')

