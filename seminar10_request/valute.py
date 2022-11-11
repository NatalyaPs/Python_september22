import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
print(data)

print(data['Valute']['USD']['Name'])
print(data['Valute']['USD']['Value'])
# ------------------------------------------
# name = data['Valute']['USD']['Name'] # создаем переменную для бота
# val = data['Valute']['USD']['Value'] # создаем переменную для бота
# print(name)
# print(val)

# # пример преподавателя:
# print(data['Valute']['USD']['Name'], data['Valute']['USD']['Value'])



