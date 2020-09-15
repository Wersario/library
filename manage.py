import requests
import os
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin


def download_text(url, filename, folder):
    base = '/Users/Юрис/Desktop/library/'
    ans = requests.get(url)
    ans.raise_for_status()
    final_filename = os.path.join(base, folder, sanitize_filename(filename) + ".txt")
    with open(final_filename, "w", encoding="UTF-8") as my_file:
        my_file.write(ans.text)


def download_image(url, filename, folder):
    base = '/Users/Юрис/Desktop/library/'
    ans = requests.get(url)
    ans.raise_for_status()
    final_filename = os.path.join(base, folder, filename.split('/')[-1])
    with open(final_filename, "wb") as my_file:
        my_file.write(ans.content)


os.makedirs("/Users/Юрис/Desktop/library/books", exist_ok=True)
os.makedirs("/Users/Юрис/Desktop/library/images", exist_ok=True)
for i in range(1, 11):
    text_url = f'http://tululu.org/txt.php?id={i}'
    html_url = f'http://tululu.org/b{i}/'
    main_ans = requests.get(html_url, allow_redirects=False)
    main_ans.raise_for_status()
    if main_ans.status_code // 100 == 2:
        response = requests.get(html_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
#        image_filename = soup.find('div', class_='bookimage').find('img')['src']
#        file_image = urljoin('http://tululu.org/', image_filename)
        text_filename = soup.find('div', id='content').find('h1').text.split(' :: ')[0].strip()
        genres_list = soup.find('span', class_='d_book').find_all('a')
        print("Заголовок:", text_filename)
        for j in genres_list:
            print(j.text)
#        download_text(text_url, text_filename, 'books/')
#        download_image(file_image, image_filename, 'images/')

