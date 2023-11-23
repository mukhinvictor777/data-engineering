"""
Задание 1
Загрузите матрицу из файла с форматом npy. Подсчитайте сумму всех элементов и их среднее арифметическое, подсчитайте сумму и среднее арифметическое главной и побочной диагоналей матрицы. Найдите максимальное и минимальное значение. Полученные значения запишите в json следующего формата:
{
    sum: 4,
    avr: 4,
    sumMD: 4, // главная диагональ
    avrMD: 5,
    sumSD: 4, // побочная диагональ
    avrSD: 5,
    max: 4,
    min: 2
}
Исходную матрицу необходимо нормализовать и сохранить в формате npy.
"""

import numpy as np
from json import dump

matrix = np.load('./1/matrix_67.npy')
size = len(matrix)

matrix_dict = {
    'sum_el': round(float((matrix.sum())), 1),
    'avr': round(matrix.mean(), 1),
    'sumMD': 0,
    'avrMD': 0,
    'sumSD': 0,
    'avrSD': 0,
    'max': round(float(matrix.max()), 1),
    'min': round(float(matrix.min()), 1)
}

for i in range(size):
    for j in range(size):
        if i == j:
            matrix_dict['sumMD'] += matrix[i][j]
        if i + j == size - 1:
            matrix_dict['sumSD'] += matrix[i][j]

matrix_dict['sumMD'] = round(float(matrix_dict['sumMD']), 1)
matrix_dict['sumSD'] = round(float(matrix_dict['sumSD']), 1)
matrix_dict['avrMD'] = round(matrix_dict['sumMD'] / size, 1)
matrix_dict['avrSD'] = round(matrix_dict['sumSD'] / size, 1)

with open('matrix_dict.json', 'w') as result:
    dump(matrix_dict, result, ensure_ascii=False, indent=4)

norm_matrix = np.ndarray((size, size), dtype=float)

for i in range(size):
    for j in range(size):
        norm_matrix[i][j] = matrix[i][j] / matrix_dict['sum_el']


print(norm_matrix[:4])