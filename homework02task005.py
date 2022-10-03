#'5. Реализуйте алгоритм перемешивания списка.

import random

print('Задайте длину списка')
n = int(input()) 
arr = []
for i in range(n):
    i = random.randint(0, 100)
    arr.append(i)
print("Список:", arr)

random.shuffle(arr)
print("Перемешанный список:", arr)
