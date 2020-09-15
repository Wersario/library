import requests
import os
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin

html_url = 'http://tululu.org/l55/'
response = requests.get(html_url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
source = soup.find('table', class_='d_book').find_all('tr')[1].find('a')['src'].text
final_link = urljoin('http://tululu.org', source)
print(final_link)