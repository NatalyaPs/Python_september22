# РАЗБОР ДОМАШНЕГО ЗАДАНИЯ КО 2 СЕМИНАРУ

# 1. на вход веществ.число ... сумма его цифр

a = input()
count = 0
for i in range(len(a)):
    if a[i] == '.':
        continue
    else:
        count += int(a[i])
print(count)


# 2.

# 1-й способ:
n = int(input())
m = 1
mass = []
for i in range (1, n+1):
    m = m*i
    mass.append(m)
print(mass)

# 2-й способ - генерация списка:
import math
n= int(input())
mass = [math.factorial(i) for i in range(1, n+1)]
print(mass)

# 3. задайте список из n чисел последовательности (1+1/n)^n и вывести на экран их суммы (^ означает степень = с степени n)
n= int(input())   # используем генерацию списков
mass = [(1+1/i)**i for i in range(1, n+1)]  # mass = [i for i in range(1, n+1)] -> заменили i на формулу из условия - то, что будем добавлять в список
print(mass)  # зачем?
print(sum(mass))

# 4.список из 2n+1 ...............
n= int(input())
mass = [i for i in range(1, n+1)]
print(mass)
mult = 1
pos = list(map(int, input().split()))
for i in pos:
    mult*=mass[i]
print(mult)

# 5. перемешив.списка
import random
mass = [i for i in range(random.randint(3,6))]
print(mass)
random.shuffle(mass)
print(mass)
