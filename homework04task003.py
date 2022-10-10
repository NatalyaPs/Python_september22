#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

nums = input('Введите числа через пробел: ').split()
list_nums = []
for i in nums:
    if i in list_nums:
        continue
    else:
        list_nums.append(i)
print(list_nums)



# метод set()
nums = input('Введите числа через пробел: ').split()
list_nums = list(set(nums))
print(list_nums)