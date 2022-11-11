import requests
from bs4 import BeautifulSoup

url = 'https://www.banki.ru/products/currency/cash/rostov-na-donu/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
mass = soup.find_all(class_ = 'table-flex_cell table-flex_cell--without-padding padding-left-default')
print(mass)
string = str(soup.find_all(class_ = 'table-flex_cell table-flex_cell--without-padding padding-left-default')[1])
print(string[string.find('>')+1 : string.find('</div') :].replace(',', '.'))