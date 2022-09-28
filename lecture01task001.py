print ('hello world')

# ПЕРЕМЕННЫЕ И ТИПЫ ДАННЫХ
# int, float, boolean, str, list, None

value = None  # если хочется объявить переменную раньше, чем дать ей значение, то используется значение None
print (type(value))
a = 123
b = 1.23
print (a)
print (b)
value = 12334
print (value)

#чтобы узнать тип данных, используем функцию type

print (type(a))
print (type(b))
print (type(value))

# строки: указываем идентификатор (имя) и через оператор присваивания (=) значение с одинарными кавычками ('')

s = 'hello world'
print (s)
s1 = "hello 'world"   # если внутри строки надо использовать разные кавычки
s2 = 'hello "world'
print (s1)
print (s2)

# ИНТЕРПОЛЯЦИЯ

print (a, b, s)
print (a, '-', b, '-', s)  # вставляем между значениями 'строки'
print ('{} - {} - {}'. format(a, b, s))  # форматированнный вывод
print ('{1} - {2} - {0}'. format(a, b, s))  # можно как в массиве индексами задать порядок
print (f'{a} - {b} - {s}')  # интерполяция

# ЛОГИЧЕСКАЯ ПЕРЕМЕННАЯ (True  или  False)

f = True
print (f)

# СПИСКИ (вместо массивов). т.к.в пайтон динамическая типизация, в списках могут быть данные разных типов (числоб строки...). Но не надо

list = []
print (list) # можно вывести пустой список
list1 = [1, 2, 3] # числа
print(list1)
list2 = ['1', '2', '3', 'hello'] # строки
print(list2)
list3 = ['1', '2', 'hello', 1, 2, 3, 4.5, True] # т.к.в пайтон динамическая типизация, в списках могут быть данные разных типов (числоб строки...). Но не надо

# пробел в начале строки может поломать код. Будет ошибка


# ВВОД И ВЫВОД ДАННЫХ
# ПРЕОБРАЗОВАНИЕ ТИПОВ

print() # отвечает за вывод данных
input() # отвечает за ввод данных от пользователя

# --------
print('Введите а');
a = input()    # будет считывать, как строку по умолчанию
print('Введите b');
b = input()    # будет считывать, как строку по умолчанию
print(a, b)
print('{} {}'. format(a,b))
print(f'{a} {b}')
print(a, '+', b, '=', a+b) # выведет по умолчанию как строки. Т.е. если а=10, b=20, то вывод в консоли будет 1020, а не 30

print('Введите а');
a = int(input())      # добавляем int или float, ч.б. на выводе получили арифметическую сумму a+b
print('Введите b');
b = int(input())      # добавляем int или float, ч.б. на выводе получили арифметическую сумму a+b
print(a, '+', b, '=', a+b)

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
#  +,  -,  *,  /,  %,  //,  **   Приоритет: **, плюс в кружочке , - в кружочке, *, /, //, %, +, -  СКОБКИ меня.т приоритет ()

x = 123
#y = 321
y = -321 # унарный минус, есть и унарный +, к-й обычно не пишется, например +123, а пишем просто 123
z = x+y
print(z)

m = 2
n = 8
c = m/n # работает как для веществ.чисел с запятой (float), т.к. выведет 0,25

k = 12
h = 8
v = k // h  # деление в целых числах, т.е.выведет не 1,5, а 1

d = 12
r = 8
e = d % r # остаток от деления, т.е. выведет 4

u = 2
p = 8
o = u ** p  # возведение в степень чеез две **, т.е. 2 в восьмой степени = 256
print(o)

q = 1.32323
w = 3
g = round(q * w, 3) # round округляет, если без аргумента(н-р 3) в скобках или написать, сколько знаков после запятой показать
print(g)

# СОКРАЩЕННЫЕ ОПРЕАЦИИ ПРИСВАИВАНИЯ

t = 3
t += 5  # это t = t + 5...... так же и с другими арифметич.действиями

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ
#  >,  >=,  <,  <=,  ==,  !=
#  not,  and,  or  - не путать с  &, |, ^
#  ещё: is, is not, in, not in

aa = 1 > 4
print (aa)  # False.     так же и с другими операциями. например 1 != 2 и т.д

bb = 1 < 4 and 5 > 2
print(bb)  # True

ff = 'qwe'
gg = 'qwe'
print( ff == gg)  # True.   Можем сравинивать СТРОКИ. Получили Истину

hh = [1, 2]
kk = [1, 2]
print (hh == kk) # True.  Можем сравнивать СПИСКИ

mm = 1 < 3 < 5 
print(mm)   # True. Можем использовать тройные (и больше) неравенства

func = 1
T = 4
X = 2
print(func < T > (X))  # тройное неравенство. Скобки у (X) можем опустить: (funk<T>X)

jj = 1 > 2 or 4 < 6
print(jj)   # логич.операц. - True, т.к. дизъюнкция: истина, если хотя бы 1 истина (or)

vv = [1, 2, 3, 4]
print (vv)
print (2 in vv)    # True - истина, т.к. 2 есть в этом списке
print (not 2 in vv)    # False - ложь, т.к. 2 есть в этом списке

is_odd = vv[0] % 2 == 0  # проверка на четность
print(is_odd)   # False, т.к. 1 нечетное число

is_odd_1 = not vv[0] % 2  # по умолчание 0-это ложь, а 1-это истина, как и в С#
print(is_odd_1)  # False. т.к. там единица. Отрицание единицы - это 0, а 0-это False


# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ.   лОГИЧЕСКИЕ ВЕТВЛЕНИЯ
#  if,  if - else            отступы важны !!!!!

username = input('Введите имя: ')
if(username == 'Маша'):
    print('Ура! Это же МАША!')
else:
    print('Привет, ', username)


aaa = int(input('a = '))     # сравнение 2х чисел
bbb = int(input('b = '))
if aaa > bbb:
    print(aaa)
else:
    print(bbb)


username = input('Введите имя: ')
if(username == 'Маша'):
    print('Ура! Это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)
    

# ЦИКЛЫ                       отступы важны !!!
#  while,   for

original = 23   
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print (inverted)      # получаем 32


original1 = 231   
inverted1 = 0
while original1 != 0:
    inverted1 = inverted1 * 10 + (original1 % 10)
    original1 //= 10
else:
    print('Пожалуй')   # когда цикл закончится, перейдем к блоку else
    print('хватит )')
print (inverted1)      # получаем 132


for i in 1, 2, 3, 4, 5:
    print(i**2)         # показать квадрат числа 


list_10 = [6,7,8]
for i in list_10:
    print(i**2)


r = range(10)       # range - объект
for i in r:
    print(i)    # вывод чисел от 0 до 9


for i in range(5):   # или сразу пишем range в цикле, не создавая переменную:
    print(i)    # вывод чисел от 0 до 4


for i in range(1, 5):   # можно указать диапазон
    print(i)    # вывод чисел от 1 до 4


for i in range(1, 10, 2):   # третим аргументом показывается приращение (здесь не на 1, а на 2)
    print(i)    # вывод: 1 3 5 7 9


for i in 'qwerty':  # в качестве итерируемого объекта могут быть СТРОКИ
    print(i)    # вывод покажет буквы в этом примере, можно пробелы, знаки ...


#   СТРОКИ  (немного о строках)

text = 'съешь еще этих мягких французских булок'
print(len(text)) # 39 -количество символов в строке
print('еще' in text)  # True -наличие подстоки (еще) в строке (text)
print(text.isdigit())   # False - являются ли все символы числами
print(text.islower())   # True - явл-ся ли символы нижним регистром
print(text.replace('еще', 'ЕЩЕ'))   # заменить
for c in text:
    print(c)


#  есть возможность воспользоваться ПОДСКАЗКАМИ языка Пайтон:

#          например:   help(text.istitle) - покажет что делает функция iatitle
#          или help(int)
#          после этого в консоли горит двоеточие. Чтобы выйти из этого блока
#          ставим курсор и нажимаем  q


# работа со СРЕЗАМИ:

text = 'съешь еще этих мягких французских булок' # строка как "массив" символов
print(text[0])         # c
print(text[1])         # ъ
# print(text[len(text)]) # IndexError, т.к. индексация с нуля
print(text[len(text)-1]) # к - первый элемент с конца строки
print(text[-5])        # б - пятый элемент с конца строки
print(text[:])         # Print(text), т.е. по умолчанию все символы в диапазоне от 0 до -1 (весь текст): print(text[0:len(text)-1])
print(text[:2])         # съ, т.е. от нулевого символа до второго. Можно от 2-го до 5-го [2:5]
print(text[len(text)-2:]) # ок
print(text[2:9])       # ешь еще
print(text[6:-18])     # еще этих мягких
print(text[0:len(text):6]) # сеикакл - каждый шестой символ во всей строке
print(text[::6])       # сеикакл
text = text[2:9] + text[-5] + text[:2]   #...


#  СПИСКИ

numbers = [1,2,3,4,5]
print(numbers)           # [1,2,3,4,5]

numbers = list(range(1,6))   # list(range) - это приведение типа range к типу list
print(numbers)           # [1,2,3,4,5]

numbers[0] = 10
print(numbers)           # [10,2,3,4,5]
print(f'{len(numbers)} len')  # 5 len - 5 элементов (длина)

for i in numbers:
    i *= 2               # в текущую переменную i кладем значение i=i*2, но НЕ в сам список !!!
    print(i)             # [20,4,6,8,10]
print(numbers)           # [10,2,3,4,5]



colors = ['red', 'green', 'blue']
for e in colors:
    print(e)          # red green blue

for e in colors:
    print(e*2)          # redred greengreen blueblue

colors.append('gray')   # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # True

colors.remove('red')   # del colors[0]   # удалить элемент

#del colors[0]  # то же, что и colors.remove('red)


#  ФУНКЦИИ   - начинаются с def

def f(x):
    if x == 1:         # можно в одной переменной разные типы использовать (int, float,..)
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))        
print(type(f(arg)))  # тип переменной 'str' - строка

arg = 2.3
print(f(arg))
print(type(f(arg)))  # тип переменной 'int'

arg = 5
print(f(arg))
print(type(f(arg)))  # тип переменной 'NoneType' - ничего