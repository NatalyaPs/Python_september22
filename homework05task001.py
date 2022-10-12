# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

import random
# ИГРА - ЧЕЛОВЕК С ЧЕЛОВЕКОМ
print()
print('На столе 2021 конфета. \nКаждый участник берет от 1 до 28 конфет за один ход.\nВсе конфеты достанутся тому, кто сделает последний ход')
player_1 = input('Первый участник игры, как вас зовут? ')
player_2 = input('Второй участник игры, как вас зовут? ')
rnd = random.randint(1,2) # первый ход
print(f'Посмотрим, чей первый ход: {rnd} участник')
if rnd == 1:
    print(f'{player_1}, ваш ход!')
else:
    print(f'{player_2}, ваш ход!')

count_player_1 = 0
count_player_2 = 0
count_candies = 117 # для проверки количество уменьшено с учетом равенства отатка от деления %28 =5 (2021, 117)


while count_candies > 0:

    if rnd == 1:
        print(f'Сейчас на столе {count_candies} конфет')
        step = int(input(f'{player_1}, cколько конфет возьмёте? '))
        while step <= 0 or step > 28:
            step = int(input(f'{player_1}! Уточните количество конфет '))
        while step > count_candies:
            step = int(input(f'{player_1}! Проверьте, сколько конфет осталось на столе )'))
        count_player_1 += step
        count_candies -= step
        rnd = False

    else:
        print(f'Сейчас на столе {count_candies} конфет')
        step = int(input(f'{player_2}, cколько конфет возьмёте? '))
        while step <= 0 or step > 28:
            step = int(input(f'{player_2}! Уточните количество конфет '))
        while step > count_candies:
            step = int(input(f'{player_2}! Проверьте, сколько конфет осталось на столе )'))
        count_player_2 += step
        count_candies -= step
        rnd = True

if count_player_1 > count_player_2:
    print(f'Победитель - {player_1}!')       
else:
    print(f'Победитель {player_2}!') 

# ИГРА - ЧЕЛОВЕК С БОТОМ:
print()
print('На столе 2021 конфета. \nКаждый участник берет от 1 до 28 конфет за один ход.\nВсе конфеты достанутся тому, кто сделает последний ход')
player_1 = input('Как вас зовут? ')
player_2 = 'бот'
print(f'{player_1}, ваш соперник - {player_2}')
rnd = random.randint(1,2) # первый ход
print(f'Посмотрим, чей первый ход (если 1, то ходит {player_1}, а если 2 - {player_2}):  {rnd} ')
if rnd == 1:
    print(f'Первый ход - {player_1}')
else:
    print(f'Первый ход - {player_2}')

count_player_1 = 0
count_player_2 = 0
count_candies = 117 # для проверки количество уменьшено с учетом равенства отатка от деления %28 =5 (2021, 117)


while count_candies > 0:

    if rnd == 1:
        print(f'Сейчас на столе {count_candies} конфет')
        step = int(input(f'{player_1}, cколько конфет возьмёте? '))
        while step <= 0 or step > 28:
            step = int(input(f'{player_1}! Уточните количество конфет '))
        while step > count_candies:
            step = int(input(f'{player_1}! Проверьте, сколько конфет осталось на столе )'))
        count_player_1 += step
        count_candies -= step
        rnd = False

    else:
        print(f'Сейчас на столе {count_candies} конфет')
        step = random.randint(1, 29)
        print(f'Бот забирает {step} конфет')
        count_player_2 += step
        count_candies -= step
        rnd = True

if count_player_1 > count_player_2:
    print(f'Победитель - {player_1}!')       
else:
    print(f'Победитель - {player_2}!') 
