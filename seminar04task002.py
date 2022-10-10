# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python(sympy)

# решение Юли:
def equad(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        print(x1, x2)
    elif d == 0:
        x1 = -b / (2*a)
        print(x1)
    else:
        print('корней нет')

equad(2, -9, 7) # 3.5  1.0

# пример преподавателя через библиотеку sympy:  ---- у меня работает в онлайне на trinket.io
import sympy
#x**2 + 4*x + 4
x = sympy.Symbol('x')  # метод Symbol определяет переменную (у нас X)
f = input()
print(sympy.solve(f, x))  # метод solve выводит корни уравнений
# ввод  x**2 + yx + 4   вывод [-2]
# ввод x**2 + 4*x + 3   вывод [-3, 1]

