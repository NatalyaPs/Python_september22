#Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.

from model import add_employees, find_employees, changes_employees
from logger import write_employees, read_employees, rename_data, write_re

print('Выбери режим работы с данными сотрудников: ')
print('1. Внести данные нового сотрудника\n2. Поиск данных сотрудника по базе\n3. Вывести список всех сотрудников на экран\n4. Внести изменения')

mode = int(input())
if mode == 1:
    a = add_employees()
    write_employees(a)

elif mode == 2:
    print(find_employees(read_employees()))

elif mode == 3:
    print(read_employees())

elif mode == 4:
    mass = read_employees()
    write_re(changes_employees(mass)) # было так: write_re(changes_employees(mass))

else:
    print('Введено неверное значение!')





















