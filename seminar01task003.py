# Напишите программу, которая на вход принимает 5 чисел 
# и находит максимальное из них.

#c1 = int(input())
#c2 = int(input())
#c3 = int(input())
#c4 = int(input())
#c5 = int(input())

c1 = int(input())       # работает. Находит максимальное число
max = c1
for i in range(4): #введем переменные в цикле
    c1 = int(input())  #  a = int(input())
    if c1 > max:       #  if a > max:
        max = c1       #  max = a
print(max)


# через список

a = list(map(int, input().split())) # сплит разделяет строку символом (пробелом), а мэп ....., лист - перевод в массив
print(a)   # не получился результат. просто через пробел ввела числа....????


# функция max
a = list(map(int, input().split()))     # можно через пробел ввести любое количество чисел
maximum = max(a)
print(maximum)


# # решение в 1 строку
# print(max(list(map(int, input().split()))))
