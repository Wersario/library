import requests
import os
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename


def download_text(url, filename, folder):
    base = '/Users/Юрис/Desktop/library/'
    fin_filename = os.path.join(base, folder, sanitize_filename(filename))
    ans = requests.get(url)
    ans.raise_for_status()
    with open(fin_filename, "w", encoding="UTF-8") as my_file:
        my_file.write(ans.text)


os.makedirs("/Users/Юрис/Desktop/library/books", exist_ok=True)
for i in range(1, 11):
    text_url = f'http://tululu.org/txt.php?id={i}'
    html_url = f'http://tululu.org/b{i}/'
    main_ans = requests.get(text_url, allow_redirects=False)
    main_ans.raise_for_status()
    if main_ans.status_code // 100 == 2:
        response = requests.get(html_url)
        soup = BeautifulSoup(response.text, 'lxml')
        title_and_author = soup.find('div', id='content').find('h1').text
        filename = title_and_author.split(' :: ')[0].strip()
        fin_filename = filename + ".txt"
        download_text(text_url, fin_filename, 'books/')

