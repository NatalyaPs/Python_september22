# 2) Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# [''ffff'.'3rfhg','4'] -> YES

list1 = ['ffff', '3rfhg','4']
# result = 'No'               # этот код у меня не работает. Вроде только в версии 3.3 работает? НО КОД РАБОЧИЙ!
# for i in list1:
#     try:
#         int(i)
#         result = 'Yes'
#         break
#     exept:
#         pass
# print (result)
#--------------
# for i in list1:
#     # #if list1.count(i) == int(i):
#     # if list1[i] == int(i):
#     #     print('Yes')
#     # else:
#     #     print('No')
#     if list1[i] == int(i):
#         print('yes')
#     else:
#         print('no')
#---------------------
# for i in list1:
#     if type(list1) == int:
#         print('yes')
#     else:
#         print('no')
#----------------------------
for i in list1:
    if i.isdigit():
        print('yes')
    else:
        continue   # print('no') -> печатает пошагово "no no yes" по каждому элементу