# 2, Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input('Введите число: '))
mult = 2
list_mult = []
while mult * mult <= num:
    if num % mult == 0:
        list_mult.append(mult)
        num //= mult
    else:
        mult += 1
list_mult.append(num)  # крайнее простое число
print("Cписок простых множителей: ", list_mult)


# решение преподавателя:
from sympy import isprime
def dev_for_primes(a):
    primelist = []
    for i in range(2, a):
        if isprime(i) and a%i == 0:
            while a%i == 0:
                primelist.append(i)
                a //= i
    return primelist
a = int(input())    # 144 -> [2,2,2,2,3,3]