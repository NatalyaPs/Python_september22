# Дана функция f(x) = 5x^2 + 10x - 30
# 1 Определить корни
# 2 Найти интервалы, на которых функция возрастает
# 3 Найти интервалы, на которых функция убывает
# 4 Построить график
# 5 Вычислить вершину
# 6 Определить промежутки, на котором f > 0
# 7 Определить промежутки, на котором f < 0

import sympy
import matplotlib

# 1. Определить корни
x = sympy.Symbol('x')
a = sympy.solve(5*x**2 + 10*x - 30, x)
print(a)

# 2. Найти интервалы, на которых функция возрастает
print(sympy.solve(5*x**2 + 10*x - 30 > 0, x))

# 3. Найти интервалы, на которых функция убывает
print(sympy.solve(5*x**2 + 10*x - 30 < 0, x))

# 4 см.ниже

# 5. Вычислить вершину
f = 5*x**2 + 10*x - 30
diff = sympy.diff(f, x)
print(diff)
print(sympy.solve(diff, x))

# 6. Определить промежутки, на котором f > 0
print(sympy.solve(diff > 0, x))

# 7. Определить промежутки, на котором f < 0
print(sympy.solve(diff < 0, x))

# 4. Построить график
sympy.plotting.plot(5*x**2 + 10*x - 30, x) # ValueError: The TextBackend supports only one graph per Plot. => import matplotlib помог

#==============================================================

# a = 5
# b = 10
# c = -30 

# # 1. нахождение корней равнения
# # 1.1 дискриминант
# def diskr(a, b, c):
#     return (b**2-4*a*c)

# # 1.2 корни уравнения
# def solve(a, b, c):
#     d = diskr(a, b, c)
#     if d < 0:
#         return 'Корней нет'
#     elif d == 0:
#         return -b/(2*a)
#     else:
#         return (-b+d**0.5)/(2*a), (-b-d**0.5)/(2*a)


# # a = int(input()) # задала вверху значения, ч.б. не вводить постоянно
# # b = int(input())
# # c = int(input())
# print(solve(a, b, c)) # 5 10 -30

# # 5. нахождение вершины
# def top_h (a, b, c):
#     return -b/(2*a)

# # 2, 3 возрастание и убывание функции
# def upnd(a, b, c):
#     # global a, b, c
#     return f'убывание на промежутке (-беск; {top_h(a, b, c)}, возрастание на ({top_h(a, b, c)}); +беск)'

# x = sympy.Symbol('x')
# sympy.plotting.plot(5*x**2 + 10*x - 30, x)
# a = sympy.solve(5*x**2 + 10*x - 30, x)
# print(a)
# i = (a[0]+a[1])/2
# if 5*i**2 + 10*i -30 > 0:
#     print(f'f больше 0 на {a[0]}; {a[1]}')
# else:
#     # .............................. 

# # или просто через sympy:
# print(5*x**2 + 10*x - 30 > 0, x)
# print(5*x**2 + 10*x - 30 < 0, x)

