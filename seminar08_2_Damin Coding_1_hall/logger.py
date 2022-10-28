# запись в файл
def write_data(a):
    with open ('base.txt', 'a', encoding='utf-8') as base:
        base.write(f'{a}\n')

# показать весь список
def read_data(a):
    with open ('base.txt', 'r', encoding='utf-8') as base:
        base.read(f'{a}\n')

# поиск
def find_data(a):
    with open ('base.txt', 'r', encoding='utf-8') as base:
        base.readline(a)

# изменить
def change_data(a):
    