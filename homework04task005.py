# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5
# 3*x² +10*x + 6
# Вывод: 5*x² + 14*x + 11

import sympy
x = sympy.Simbol('x')

with open("file_hw_4_5_1.txt", 'r') as data_1:  # сокращенное название нашего файла
    a = data_1.read()
print(a)

with open("file_hw_4_5_2.txt", 'r') as data_2:  # сокращенное название нашего файла
    b = data_2.read()
print(b)

c = sympy.simplify(a + '+' + b) # сложение обязательно знaк '+'
with open("file_hw_4_5_3.txt", 'w') as data_3:
    data_3(str(c))
print(c)





# data_1 = open('file_hw_4_5_1.txt', 'r')
# data_2 = open('file_hw_4__5_2.txt', 'r')

# with open("file_hw_4_4.txt", 'w') as f:
#     f.write(formula)