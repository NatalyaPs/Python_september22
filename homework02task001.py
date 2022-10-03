# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

a =float(input('Введите число: '))
if a < 0:
    a = a*(-1)
a=str(a)
a=a.replace('.', '')
a=list(a)
# print(a)
sum=0
for i in range(len(a)):
    sum+=int(a[i])
print("Сумма цифр =", sum)

# РЕШЕНИЕ ПРЕПОДАВАТЕЛЯ:
# a=input()
# count=0
# for i in range(len(a)):
#     if a[i] == '.':
#         continue
#     else:
#         count+=int(a[i])
# print(count)