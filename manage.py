import requests
import os


os.makedirs("/Users/Юрис/Desktop/library/books", exist_ok=True)
for i in range(1, 11):
    url = f'http://tululu.org/txt.php?id={i}/'
    ans = requests.get(url, allow_redirects=False)
    if((ans.status_code // 100) == 2):
        print("OK")
        with open(f"/Users/Юрис/Desktop/library/books/id{i}.txt", "w") as my_file:
            my_file.write(ans.text)

