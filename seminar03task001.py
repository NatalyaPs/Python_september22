# 1)Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.
# [1,2,3,4,4,5,5,6] -> [1,2,3,6]

list1 = [1,2,3,4,4,5,5,6]
list2 = []
for i in list1:
    if list1.count(i) == 1:
        list2.append(i)
print(list2)