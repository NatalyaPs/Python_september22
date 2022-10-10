# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# Ввод: 2 3 5 -> 2 5

# import sympy
# решение Юлии
# from random import random


numbers = input('Введите числа через пробел: ').split()
min = int(numbers[0])
max = int(numbers[0])
for i in range(len(numbers)):
    if int(numbers[i]) > max:
        max = int(numbers[i])
    if int(numbers[i]) < min:
        min = int(numbers[i])
print(min, max)

# решение Юрия: ------  в моей версии не работает, а в онлайне работает
# функция для ввода:
def input_nums (log = 'Введите строку из набора чисел, разделенных пробелами: '):
    try:
        return list(map(int, input(log).split()))
    except:
        return input_nums('Введены не целые числа или не числа. Попробуйте еще: ')
# функция - решение:
def get_min_max(lst):
    return(min(lst), max(lst))

nums = input_nums()  # 1 2 3 4 5 6
print(get_min_max(nums)) # (1, 6)

# решение Рустама Ибрагимова:
import random
length = int(input('Введите количество чисел -> '))
min_limit = int(input('Введите нижнюю границу -> '))
max_limit = int(input('Введите верхнюю границу -> '))
list_check = [random.randint(min_limit, max_limit) for i in range(length)]
print(f'{list_check} -> {max_limit} {min_limit}') # [82, 21, 14, 48, 41] -> 82  14


