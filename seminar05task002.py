# 36/ Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

nums = [1, 5, 2, 3, 4, 6, 1, 7]

def get_up(nums):
    uplist = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in uplist:
            uplist.append(nums[i])
    return uplist

print(get_up(nums))
