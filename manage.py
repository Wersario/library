import requests
from bs4 import BeautifulSoup

url = 'http://tululu.org/b1/'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
main_inf = soup.find('div', id='content').find('h1').text
inf_list = main_inf.split(' :: ')
print("Заголовок:", inf_list[0].strip())
print("Автор:", inf_list[1].strip())