# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

a = []
print('Задайте длину списка')
n = int(input()) 

for i in range(n):
    i = random.randint(0, 10)
    a.append(i)
print(a)

sum = 0
for i in range(len(a)):
    if i % 2 != 0:       #not i % 2:
        sum += a[i]
print("Сумма элементов списка на нечетных позициях:" , sum)


#решение преподавателя:
def sum0funeven (mass):
    count = 0
    for i in range(1, len(mass), 2):  #шаг =2, ч.б.идти по нечетным и не делать проверку на четность. Поэтому и начинаем с 1
        count += mass[i]
    print(count)

a = [random.randint(1, 10) for i in range(5)] # генерация списка случайных чисел, размер списка =5
print(a)
sum0funeven(a)