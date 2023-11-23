"""
Задание 2
Загрузите матрицу из файла с форматом npy. Создайте три массива.
Отберите из матрицы значения, которые превышают следующее значение следующим образом:
индексы элемента разнесите по массивам  , а само значение в массив  .
Сохраните полученные массив в файла формата npz.
Воспользуйтесь методами np.savez() и np.savez_compressed(). Сравните размеры полученных файлов.
"""

import numpy as np
from os.path import getsize

matrix = np.load('./2/matrix_67_2.npy')
size = len(matrix)

x = np.array([i for i in range(0, size)])
y = np.array([i for i in range(size)])
z = np.array([matrix[i][j] for i in range(len(x)) for j in range(len(y))])

np.savez('task_2', x=x, y=y, z=z)
np.savez_compressed('task_2_zip', x=x, y=y, z=z)

print(f'points = {getsize('task_2.npz')}')
print(f'points = {getsize('task_2_zip.npz')}')
