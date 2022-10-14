# предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
ls = list(map(int, input('Введите элементы списка через пробел :').split()))
print(ls)
sum = sum([ls[i] for i in range(1, len(ls), 2)])
print(sum)