# задача 2. напишите программу, которая принимает на вход 2 числа и проверяет, является ли одно число квадратом другого

#print ('введите число а: ')
a = int(input())

#print ('введите число b: ')
b = int(input())

if a**2 == b or b**2 == a:
    print ('Yes')
#elif b**2 == a
    #print ('Yes')
else:
    print('No')




#  ===================================

c = input().split()  # метод -числа вводятся через пробел \ если split(',') то через запятую. 
a = int(c[0])
b = int(c[1])