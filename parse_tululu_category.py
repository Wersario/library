import requests
import os
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin

for j in range(0, 4):
    html_url = f'http://tululu.org/l55/{j}/'
    response = requests.get(html_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    pre_sources_list = soup.find_all('table', class_='d_book')
    for i in pre_sources_list:
        final_source = urljoin('http://tululu.org', i.find('a')['href'])
        print(final_source)