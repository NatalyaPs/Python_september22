# '3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = [1.1, 1.2, 3.1, 5, 10.01]   # 5 -> 5.0
arr = []
for i in a:
    i = round(i%1, 2)
    arr.append(i)
print("Дробные части: ", arr)

print("Разница между максим.и миним.:", max(arr) - min(arr))

