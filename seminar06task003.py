# Цифровой корень — это рекурсивная сумма всех цифр числа.
# Учитывая n, возьмите сумму цифр n. 
# Если это значение имеет более одной цифры, 
# продолжайте уменьшать таким образом, пока не будет получено 
# однозначное число. Ввод будет неотрицательным целым числом.
# Примеры
# 16 --> 1 + 6 = 7
# 942 --> 9 + 4 + 2 = 15 --> 1 + 5 = 6
# 132189 --> 1 + 3 + 2 + 1 + 8 + 9 = 24 --> 2 + 4 = 6
# 493193 --> 4 + 9 + 3 + 1 + 9 + 3 = 29 --> 2 + 9 = 11 --> 1 + 1 = 2

def summ(a):
    if a < 10:
        return a
    else:
        return summ(sum(map(int, list(str(a))))) # рекурсия
print(summ(493193))

# или второй вариант:

def s(a):  # функция 1 => сумма цифр в числе
    sum = 0
    for i in str(a):
        sum += int(i)
    return sum

def summ(a):  # рекурсия
    if a < 10:
        return a
    else:
        print(s(a))  # покажет промежуточные суммы. Это не обязательно
        return summ(s(a)) # в этй функции еще функция по поиску суммы цифр в числе

print(summ(493193))

