def add_data():
    id = input('Введите id: ')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    post = input('Введите должность: ')
    salary = input('Введите оклад: ')
    directory = f'{id}||{name}||{surname}||{phone}||{post}||{salary}\n'
    return directory
    

def find_data(f):   
    a = input('Введите данные для поиска: ')
    find = list(filter(lambda x: a in x, f.split('\n')))
    find = '\n'.join(find)
    return find
    

# надо вставить в документ строку после редактирования. 
# у меня сейчас удаляет исходные данные и заменяет их на исправленную строку
# нужно вставить в цикл
def change_data(c):
    a = input('Данные сотрудника для редактирования: ')
    find = list(filter(lambda x: a in x, c.split('\n')))
    find = '\n'.join(find)
    print(f'редактировать: {find}')
     
    find = find.split('||')  # edit = find.split('||')
    print(find)

    new_value = int(input(('Выберите, какие изменения сделать:\n \
        1 - изменить ip\n \
        2 - изменить имя\n \
        3 - изменить фамилию\n \
        4 - изменить телефон\n \
        5 - изменить должность\n \
        6 - изменить оклад\n')))
    if new_value == 1:
        find[0] =  input('Новое значение для ID: ')     # edit
        print(f'Новые данные: {find}')                  # edit
    elif new_value == 2:
        find[1] = input('Новое значение для ИМЯ: ')
        print(f'Новые данные: {find}')
    elif new_value == 3:
        find[2] = input('Новое значение для ФАМИЛИЯ: ')
        print(f'Новые данные: {find}')
    elif new_value == 4:
        find[3] = input('Новое значение для ТЕЛЕФОН: ')
        print(f'Новые данные: {find}') 
    elif new_value == 5:
        find[4] = input('Новое значение для ДОЛЖНОСТЬ: ')
        print(f'Новые данные: {find}')    
    elif new_value == 6:
        find[5] = input('Новое значение для ОКЛАД: ')
        print(f'Новые данные: {find}')
    else:
        print('Уточните, какие изменения хотите внести')

    find = '||'.join(find) + '\n'
    return find






