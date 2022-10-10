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




#----------------- 
lst = [1, 5, 2, 3, 4, 6, 1, 7]
lst2 = [5, 4, 3, 2, 1, 0, -1, -2]
lst3 = [1, 1, 1, 1, 1, 1, 1, 1]

def make_new_list(old_list):
    new_list = []
    for i in range(len(old_list)):
        if i == 0 or old_list[i] > new_list[-1]:
            new_list.append(old_list[i])
    return new_list

print(make_new_list(lst), make_new_list(lst2), make_new_list(lst3))
