# 37. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# Пример: абв абвгд гдеёжз непшщтг -> гдеёжз непшщтг

my_text = 'абв абвгд гдеёжз непшщтг'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)
