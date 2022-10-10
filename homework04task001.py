# 1. Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# формула Лейбница x=4-4/3+4/5-4/7+4/9-...
d = int(input('Введите желаемую точность: '))  # 10000
k = 1                  # знаменатель
sum = 0                # меняется + -
for i in range(d):
    if i % 2 == 0:
        sum += 4 / k
    else:
        sum -= 4 / k
    k += 2
print(sum)


# метод acos()
from math import acos    # ----- работает в онлайн
d = int(input('Введите нужную точность: ')) # 3
pi = round(2*acos(0.0), d)
print(pi)

# # -------
# import math
# print(math.pi)
