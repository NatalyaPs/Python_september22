
def add_contact():
    name = input('Введите имя: ')
    first_name = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    directory = name + ' ' + first_name + '||' + phone + '\n'
    return directory

def find_contact(f):  # поиск 
    a = input('Введите данные для поиска: ')
    find = list(filter(lambda x: a in x, f.split('\n')))
    # print(find)
    return find

# def save_contact():

