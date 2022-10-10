# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import numpy as np                        # работает в онлайн (trinket.io)
import random
import matplotlib.pyplot as plt

k = int(input('Введите степень k: '))
coeff = []
for i in range(k+1):
  coeff.append(random.randint(0, 101))
print(coeff)
print()

formula = np.poly1d(coeff)
print(formula)

with open("file_hw_4_4.txt", 'w') as f:
    f.write(formula)


# решение преподавателя:
def gen_pol(n):
    polinom = ''
    for i in range(n+1):
        if i == 0:
            polinom += str(random.randint(1, 2)) + '*x**' + str(n-i)
        elif i == n:
            polinom += '+' + str(random.randint(1, 2))
        else:
            polinom += '+' + str(random.randint(1, n)) + '*x**' + str(n-i)
    polinom += '= 0'
    return polinom

n = int(input())


with open("generatedpol.txt", 'w') as f:
    f.write(gen_pol(n))
print(gen_pol(n))