# a = [1,2,3,4,5]
# x = sum([a[i] for i in range(1, len(a), 2)])
# print(x)
# 
# list = [i for i in range(1, 11) if i%2 ==0] # [2,4,6,8,10]
# print(list)
#================================



# # 1.
# ====================================


# # 1.1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# # Пример:
# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет
# a= int(input('введите число: '))
# if a <6 and a>=1:
#     print('будний день')
# elif a==6 or a==7:
#     print('выходной')
# else:
#     print('введите другое число')



# # 1.2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.



# # 1.3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# # Пример:
# #- x=34; y=-30 -> 4
# #- x=2; y=4-> 1
# #- x=-34; y=-30 -> 3



# # 1.4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).



# # 1.5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# # Пример:
# # - A (3,6); B (2,1) -> 5,09
# # - A (7,-5); B (1,-1) -> 7,21




# # 2.
# #==================================


# # 2.1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # *Пример:*
# # - 6782 -> 23
# # - 0,56 -> 11

# a=input('введите число: ')
# print(type(a))
# print(a)
# a=list(a)
# print(type(a))
# print(a)

# su=0

# for i in a:
#     if i == '.':
#         continue
#     else:
#         su+=int(i)
# print(su)





# # 2.2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # *Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N=int(input('N = '))
# list_N = list(range(1, N+1)) # правильнее будет (2, N+1)
# count = 1
# print(list_N)
# mult_N = []
# for i in list_N:
#     count*=i
#     #print(count) # выводит в столбик числа, а в задаче нужен список
#     mult_N.append(count)
# print(mult_N) # [ 1, 2, 6, 24 ]




# # или еще вариант со встроенной функцией math.factorial:

# import math
# N=int(input('N = '))
# print(math.factorial(N)) #24 - проверка, как выводит функция результат
# a = []
# for i in list(range(1, N+1)):
#     a.append (math.factorial(i))
# print(a) # [ 1, 2, 6, 24 ]




# # инет 1:

# n = int(input())
# factorial = 1
# for i in range(2, n+1):
#     factorial *= i
# print(factorial) # 24

# # инет 2:

# n = int(input())
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial) # 24

# # рекурсия: пример с инета = не работает .. надо разобраться
# def factor(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return factor((n-1)*n)
# #print(factor(n = int(input('n = '))))
# n=int(input('n = '))
# print(factor(n))




# # 2.3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# # *Пример:*
# # - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

# n = int(input('n = '))
# list_n = []
# for i in range(1, n+1):
#     i = (1+1/i)**i
#     list_n.append(i)
# print(list_n)



# # 2.4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

# n = int(input('n = '))
# list_n = []
# for i in range(-n, n+1):
#     list_n.append(i)
# print(F'исходный список {list_n}')

# index = list(map(int, input('укажите индексы перемножаемых элементов через пробел: ').split()))
# print(f'индексы перемножаемых элементов списка {index}')
# mult = 1

# for i in index:
#     mult *= list_n[i]   
# print(f'произведение элементов на указанных озициях -> {mult}')



# # 2.5. Реализуйте алгоритм перемешивания списка.

# import random
# #lst = list(map(int, input('введите числа через пробел: ').split()))
# lst = [i for i in range(random.randint(5, 15))] # дает список по порядку, но разной длины каждый раз
# print(lst)
# random.shuffle(lst)
# print(lst)




# # 3
# ================================



# 3.1. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = []
# data = '1 2 3 4 5 6 7 8 9'.split()
# print(data)

# def select(f, col):
#     return(f(x) for x in col)
# print(select(int, data))
# # res = select(int, data)
# # print(res)




# # =================== проба из семинара5
# показать те слова, где нет 'абв'
# my_text = 'абв абвгд абгдежз нерто'

# def del_some_worlds(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_worlds(my_text) 
# print(my_text)



# # -==============   проба с семинара 3

# # выведите только те элементы, которые встречаются 1 раз
# list_1 = [1, 2, 3, 4, 4, 5, 5, 6]
# list_2 = []
# for i in list_1:
#     if list_1.count(i) == 1:
#         list_2.append(i)
# print(list_2)

# # присутствует ли в списке строк число  -> да, нет
# list_1 = ['fff', 'hdkfkf', 'hjk6', '7']
# result = 'No'
# for i in list_1:
#     try:
#         int(i)
#         result = 'Yes'
#         break
#     except:
#         pass
# print(result)


# # ==================== семинар 6
# # выисление арифметического выражения, заданного строкой - МЕТОД  eval

# print(eval(input(2+2*8)))


# # дана последовательность чисел. получить список уникальных элементов заданной последовательности
# data = list(map(int, input().split()))
# li = list(filter(lambda i: data.count(i) == 1, data))
# print(li)



# def add_data():
#     # # id = input('Введите id: ')
#     # # name = input('Введите имя: ')
#     # # surname = input('Введите фамилию: ')
#     # # phone = input('Введите телефон: ')
#     # # post = input('Введите должность: ')
#     # salary = input('Введите оклад: ')
#     directory = list()
#     directory.append(input('Введите id: '))
#     directory.append(input('Введите имя: '))
#     directory.append(input('Введите фамилию: '))
#     directory.append(input('Введите телефон: '))
#     directory.append(input('Введите должность: '))
#     directory.append(input('Введите оклад: '))
#     # directory[0] = input('Введите id: ')
#     # directory[1] = input('Введите имя: ')
#     # directory[2] = input('Введите фамилию: ')
#     # directory[3] = input('Введите телефон: ')
#     # directory[4] = input('Введите должность: ')
#     # directory[5] = input('Введите оклад: ')
#     # directory = [id + '||' + name + '||' + surname + '||' + phone+'||' + post+ '||'+salary]
#     # return directory
#     directory = str(directory)
#     print(directory)
 

# #   print(add_data())  
# add_data()


# =====================

# def add_data():
#     id = input('Введите id: ')
#     name = input('Введите имя: ')
#     surname = input('Введите фамилию: ')
#     phone = input('Введите телефон: ')
#     post = input('Введите должность: ')
#     salary = input('Введите оклад: ')
#     directory = id + '||' + name + '||' + surname + '||' + phone+'||' + post+ '||'+salary +'\n' 
#     return directory
    
   
# # --------------------------------
# a = '1 2 3 4 5'
# print(a)

# # -----------------------------------

# def change_data(c):
#     # find_data(c)
#     # print(find_data(c))
#     a = input('Данные сотрудника для редактирования: ')
#     find = list(filter(lambda x: a in x, c.split('\n')))
#     print(find)
#     # print(type(find))
#     find = str(find)  # 111              #
#     # print(type(find))
#     # print(find)
#     # print(find[0])
#     # edit = str(find)   # 
#     # print(type(edit))
#     edit = find.split('||') #
#     print(edit)
#     print(type(edit))
#     print(edit[0])
#     print(edit[1])

#     new_value = input(('Выберите, какие изменения сделать:\n \
#         1 - изменить ip\n \
#         2 - изменить имя\n \
#         3 - изменить фамилию\n \
#         4 - изменить телефон\n \
#         5 - изменить должность\n \
#         6 - изменить оклад\n'))

#     for i in range(len(edit)):
#         if new_value == 2:
#             edit[1] = input('Новое значение для ИМЯ: ')


#     print(edit)


#     # lst = []
#     # for i in range(len(c)):
#     #     if c[i].find(data) != -1:
#     #         lst = c[i].split('||')
#     #         print(lst)

#     new_value = input(('Выберите, какие изменения сделать:\n \
#         1 - изменить ip\n \
#         2 - изменить имя\n \
#         3 - изменить фамилию\n \
#         4 - изменить телефон\n \
#         5 - изменить должность\n \
#         6 - изменить оклад\n'))
#     # print(new_value)

#     new_data = []
#     # for i in range(len(employee)):
#     new_data = employee.split('||')

#     # new_data = []
#     # for i in range(len(c)):
#     #     # if c[i].find(new_value) != -1:
#     #     new_data = c.split('||')
#     print(new_data)  # смотрим список строк

#     for i in new_data:
#         if new_data.count(i) == new_value-1:
#             i = input('Внесите изменения: ')
#             new_data = '||'.join(new_data) + '\n'

#     return new_data


# # =============================================
# edit = ['1', 'f', 'f', 'f', 'f', 'f']
# new_value = int(input(('Выберите, какие изменения сделать:\n \
#         1 - изменить ip\n \
#         2 - изменить имя\n \
#         3 - изменить фамилию\n \
#         4 - изменить телефон\n \
#         5 - изменить должность\n \
#         6 - изменить оклад\n')))

# if new_value == 1:
#     edit[0] =  input('Новое значение для ID: ')
#     print(f'Новые данные: {edit}')
# elif new_value == 2:
#     edit[1] = input('Новое значение для ИМЯ: ')
#     print(f'Новые данные: {edit}')
# elif new_value == 3:
#     edit[2] = input('Новое значение для ФАМИЛИЯ: ')
#     print(f'Новые данные: {edit}')
# elif new_value == 4:
#     edit[3] = input('Новое значение для ТЕЛЕФОН: ')
#     print(f'Новые данные: {edit}') 
# elif new_value == 5:
#     edit[4] = input('Новое значение для ДОЛЖНОСТЬ: ')
#     print(f'Новые данные: {edit}')    
# elif new_value == 6:
#     edit[5] = input('Новое значение для ОКЛАД: ')
#     print(f'Новые данные: {edit}')
# else:
#     print('Уточните, какие изменения хотите внести')   
#     #============================================================
# # надо вставить в документ строку после исправления. 
# # у меня сейчас удаляет исходные данные и заменяет их на исправленную строку
# # нужно вставить в цикл
# def change_data(c):
#     a = input('Данные сотрудника для редактирования: ')
#     find = list(filter(lambda x: a in x, c.split('\n')))
#     find = '\n'.join(find)
#     print(f'редактировать: {find}')
     
#     find = find.split('||')  # edit = find.split('||')
#     print(find)

#     new_value = int(input(('Выберите, какие изменения сделать:\n \
#         1 - изменить ip\n \
#         2 - изменить имя\n \
#         3 - изменить фамилию\n \
#         4 - изменить телефон\n \
#         5 - изменить должность\n \
#         6 - изменить оклад\n')))
#     if new_value == 1:
#         find[0] =  input('Новое значение для ID: ')
#         print(f'Новые данные: {find}')
#     elif new_value == 2:
#         find[1] = input('Новое значение для ИМЯ: ')
#         print(f'Новые данные: {find}')
#     elif new_value == 3:
#         find[2] = input('Новое значение для ФАМИЛИЯ: ')
#         print(f'Новые данные: {find}')
#     elif new_value == 4:
#         find[3] = input('Новое значение для ТЕЛЕФОН: ')
#         print(f'Новые данные: {find}') 
#     elif new_value == 5:
#         find[4] = input('Новое значение для ДОЛЖНОСТЬ: ')
#         print(f'Новые данные: {find}')    
#     elif new_value == 6:
#         find[5] = input('Новое значение для ОКЛАД: ')
#         print(f'Новые данные: {find}')
#     else:
#         print('Уточните, какие изменения хотите внести')

#     find = '||'.join(find) + '\n'
#     return find




#      # ================= попытка с циклом. ПОТОМ  ПОДУМАТЬ  ЕЩЕ :
# def change_data(c):    
#     a = input('Данные сотрудника для редактирования: ')
#     find = []
#     index = 0
#     for i in range(len(c)):
#         c[i] = list(filter(lambda x: a in x, c.split('\n')))
#         c = '\n'.join(find)
#         index = 1
#       # print(f'редактировать: {find}')
     
#     find = c.split('||')  # edit = find.split('||')
#     print(f'редактировать: {find}')

#     new_value = int(input(('Выберите, какие изменения сделать:\n \
#         1 - изменить ip\n \
#         2 - изменить имя\n \
#         3 - изменить фамилию\n \
#         4 - изменить телефон\n \
#         5 - изменить должность\n \
#         6 - изменить оклад\n')))
#     if new_value == 1:
#         find[0] =  input('Новое значение для ID: ')
#         print(f'Новые данные: {find}')
#     elif new_value == 2:
#         find[1] = input('Новое значение для ИМЯ: ')
#         print(f'Новые данные: {find}')
#     elif new_value == 3:
#         find[2] = input('Новое значение для ФАМИЛИЯ: ')
#         print(f'Новые данные: {find}')
#     elif new_value == 4:
#         find[3] = input('Новое значение для ТЕЛЕФОН: ')
#         print(f'Новые данные: {find}') 
#     elif new_value == 5:
#         find[4] = input('Новое значение для ДОЛЖНОСТЬ: ')
#         print(f'Новые данные: {find}')    
#     elif new_value == 6:
#         find[5] = input('Новое значение для ОКЛАД: ')
#         print(f'Новые данные: {find}')
#     else:
#         print('Уточните, какие изменения хотите внести')

#     find = '||'.join(find) + '\n'
#     c[index] = find
#     return c



# # КОНФЕТЫ
# import random
# rnd = 1 # первый ход юзера
# count_user1 = 0
# count_bot = 0
# count_candies = 117 # для проверки количество уменьшено с учетом равенства отатка от деления %28 =5 (2021, 117)
# whose_move = 0  # чей ход

# while count_candies > 0:
#     whose_move += 1

#     if rnd == 1:
#         print(f'Всего {count_candies} конфет\nУ вас: {count_user1}\nУ бота: {count_bot}')
#         step = int(input(f'Cколько конфет возьмёте? '))
#         while step <= 0 or step > 28:
#             step = int(input(f'{count_user1}! Уточните количество конфет '))
#         while step > count_candies:
#             step = int(input(f'{count_user1}! Проверьте, сколько конфет осталось )'))
#         count_user1 += step
#         count_candies -= step
#         rnd = False

#     else:
#         print(f'Всего {count_candies} конфет\nУ вас: {count_user1}\nУ бота: {count_bot}')
#         if count_candies <= 28:
#             step = count_candies
#             print(f'Бот забирает {step} конфет')
#         else:
#             step = random.randint(1, 29)
#             print(f'Бот забирает {step} конфет')
#         count_bot += step
#         count_candies -= step
#         rnd = True

# if whose_move %2 == 0:
#     print(f'Выиграл бот!')
# else:
#     print(f'Вы выиграли!')


