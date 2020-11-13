import requests
import os
import json
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename
from urllib.parse import urljoin


def download_json(json_file, filename):
    base = '/Users/Юрис/Desktop/library/'
    final_filename = os.path.join(base, sanitize_filename(filename) + ".json")
    with open(final_filename, "w", encoding="UTF-8") as my_file:
        json.dump(json_file, my_file, ensure_ascii=False)


def download_text(url, filename, folder):
    base = '/Users/Юрис/Desktop/library/'
    ans = requests.get(url, allow_redirects=False, verify=False)
    ans.raise_for_status()
    final_filename = os.path.join(base, folder, sanitize_filename(filename) + ".txt")
    with open(final_filename, "w", encoding="UTF-8") as my_file:
        my_file.write(ans.text)


def download_image(url, filename, folder):
    base = '/Users/Юрис/Desktop/library/'
    ans = requests.get(url, verify=False)
    ans.raise_for_status()
    final_filename = os.path.join(base, folder, filename.split('/')[-1])
    with open(final_filename, "wb") as my_file:
        my_file.write(ans.content)


main_info = []

for j in range(1, 5):
    html_url = f'https://tululu.org/l55/{j}/'
    main_response = requests.get(html_url, verify=False)
    main_response.raise_for_status()
    first_soup = BeautifulSoup(main_response.text, 'lxml')
    pre_sources_list = first_soup.find_all('table', class_='d_book')

    for z in pre_sources_list:
        final_source = urljoin('https://tululu.org', z.find('a')['href'])
        digit = z.find('a')['href'][2:-1]

        os.makedirs("/Users/Юрис/Desktop/library/books", exist_ok=True)
        os.makedirs("/Users/Юрис/Desktop/library/images", exist_ok=True)

        main_ans = requests.get(final_source, allow_redirects=False, verify=False)
        main_ans.raise_for_status()

        text_url = f'https://tululu.org/txt.php?id={digit}'
        text_ans = requests.get(text_url, allow_redirects=False, verify=False)
        text_ans.raise_for_status()
        response = requests.get(final_source, verify=False)
        response.raise_for_status()
        if text_ans.status_code // 100 == 2:

            soup = BeautifulSoup(response.text, 'lxml')
            image_filename = soup.find('div', class_='bookimage').find('img')['src']
            file_image = urljoin('https://tululu.org/', image_filename)
            text_filename = soup.find('div', id='content').find('h1').text.split(' :: ')[0].strip()
            genres_list = soup.find('span', class_='d_book').find_all('a')

            html_comments_selector = "div.content div.texts"
            html_comments_list = soup.find('div', id='content').find_all('div', class_='texts')
            comments_list = []e
            for i in html_comments_list:
                comments_list.append(i.find('span').text)

            html_genres_list = soup.find('span', class_='d_book').find_all('a')
            genres_list = []
            for i in html_genres_list:
                genres_list.append(i.text)

            info = {
                'title': sanitize_filename(text_filename),
                'author': soup.find('div', id='content').find('h1').find('a')['title'].split(' - ')[0].strip(),
                'img_scr': os.path.join('images/', image_filename.split('/')[-1]),
                'book_path': os.path.join('books/', sanitize_filename(text_filename) + '.txt'),
                'comments': comments_list,
                'genres': genres_list
            }
            main_info.append(info)

            download_text(text_url, text_filename, 'books/')
            download_image(file_image, image_filename, 'images/')

download_json(main_info, 'information')

