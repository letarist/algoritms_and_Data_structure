"""Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры."""
n = int(input('Введите количество элементов последовательности: '))
summary = 0
value_range = 1
i = 0
while i < n:
    summary += value_range
    value_range /= -2
    i += 1
print(f'Сумма членов последовательности: {summary}')