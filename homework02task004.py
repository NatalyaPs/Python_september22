#'4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

n = int(input('Введите число для списка [-n, n]: '))
arr = []
for i in range(-n, n+1):
    arr.append(i)
print("Список", arr)


print('Сколько элементов вы хотите перемножить?')
num = int(input())
mas = []
print('Введите индексы:')
for j in range(num):
    j = int(input())
    mas.append(j)
#print(mas)   

mult = 1    
for i in mas:
    mult *= arr[i]
print("Произведение указанных элементов:", mult)


#print('Для нахождения произведения элементов, введите их индексы через пробел:')
#a = list(map(int, input().split))

# p = 1
# for i in a:
#     p *= arr[i]
# print(p)