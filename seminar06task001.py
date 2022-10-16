# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# summ = lambda a, b, c: a + b + c  # надо выражения задавать строкой по условию
# mult = lambda a, b, c: a * b * c
# subandmult = lambda a, b, c: a - b * c
# divandsumm = lambda a, b, c: c + a / b

# def result (op, a, b, c):
#     print(op (a, b, c))

# result(summ, 11, 10, 9)
# result(mult, 11, 10, 9)
# result(subandmult, 11, 10, 9)
# result(divandsumm, 11, 10, 9)

# правильное решение по условию через строку:
# a = input()
# print(type(a))  # тип строка
# b = eval(a)
# print(b)

# или в одну строку:
print(eval(input()))