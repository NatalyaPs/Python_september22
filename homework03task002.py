# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# #в этом решении, если b четное, то пишет лишний раз крайнее значение, будто +1
# a = [2, 3, 5, 6]
# b = len(a)//2 if len(a)//2 == 0 else len(a)//2+1 
# arr = [a[i] * a[len(a)-i-1] for i in range(b)]
# print(len(a))
# print(b)    
# print(arr)


a = [2, 3, 4, 5, 6]
b = []
if len(a) % 2 == 0:
    for i in range(len(a) // 2):
        b.append(a[i] * a[len(a)-i-1])
else:
    for i in range(len(a) // 2 + 1):
        b.append(a[i] * a[len(a)-i-1])
print(b)
# решение преподавателя