"""Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
этих позициях первого массива стоят четные числа"""

import random

SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')
even__index_elem = []
for i in range(len(array)):
    if array[i] % 2 == 0:
        even__index_elem.append(i)

print(f'Индексы четных элементов из исходного массива: {even__index_elem}')