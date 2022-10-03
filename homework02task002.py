# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
multi = []
new = 1
for i in range(1, n+1):
    new*=i
    multi.append(new)
print("Набор произведений:", multi)


# РЕШЕНИЕ ПРЕПОДАВАТЕЛЯ:
# 1 СПОСОБ - так же
# 2 СПОСОБ:
import math
n=int(input())
mass=[math.factorial(i) for i in range(1, n+1)]
print(mass)