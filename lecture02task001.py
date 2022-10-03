# Данные, функции и модули в Pythton

colors = ['red', 'green', 'blue123'] # источник данных - здесь список
data = open('file_lec_2.txt', 'a') # связываем текущую переменную с текстовым файлом
data.writelines(colors) # разделителей не будет / writelines для записи данных
data.write('\nLINE 125\n')
data.write('LINE 135\n')
data.close() # закрыть файл - разорвать подключение файловой переменной с файлом на диске, ч.б.не было утечек памяти. Если не сделать, то может быть ошибка типа: невозможно закрыть...

# или

with open('file_lec_2.txt', 'w') as data:
    data.write('line 10\n')
    data.write('line 20\n')