# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1, 10))  # ячейки для поля
winning = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9),
           (1, 5, 9), (3, 5, 7)]  # выигрышные комбинации  виде кортежей в списке


def playing_field():         # игровое поле
    print('-------------')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')  # строки
    print('-------------')


def move_in_the_game(game_symbol):     # ход в игре
    while True:
        value = input('Выберите ячейку на поле для ' + game_symbol + ': ')
        if not (value in '123456789'):
            print('Такой ячейки нет. Попробуйте ещё ')
            continue                   # возвращаемся в начало цикла
        value = int(value)
        if str(board[value - 1]) in 'XO':  # ---------------------------------
            print('Эта ячейка уже занята')
            continue
        board[value - 1] = game_symbol
        break


def check_the_field():        # проверка поля
    for element in winning:         # element проверяем кортежи из списка winning по индексам
        if (board [element [0] - 1]) == (board [element [1] - 1]) == (board [element [2] - 1]):
            return board [element [1] - 1]  # или return True
    else:                      # else стоит не для условия, а для цикла for (если не сработала ни одна выигрышная комбинация)
        return False

def main():
    count = 0
    while True:
        playing_field()
        if count % 2 == 0:
            move_in_the_game('X')
        else:
            move_in_the_game('O')
        if count > 3:
            winning = check_the_field()
            if winning:
                playing_field()
                print(winning, "Вы выиграли!")
                break
        count += 1
        if count > 8:
            playing_field()
            print('Ничья!')
            break

main()
