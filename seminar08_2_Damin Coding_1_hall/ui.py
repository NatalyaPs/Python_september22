# Создать информационную систему позволяющую работать с 
# сотрудниками некой компании
# ввод, вывод, поиск, редактирование (+удаление).
# параментры: id, фио, телефон, должность, зарплата

def get_data ():
    id = input('Введите id сотрудника: ')
    name = input('Введите ФИО сотрудника: ')
    phone = input('Введите номер телефона сотрудника: ')
    post = input('Введите должность сотрудника: ')
    cost = input('Введите зарплату сотрудника: ')
    return (f'{id}  {name}  {phone}  {post}  {cost}\n')

def print_data(a):
    print (a)

# print(get_data())