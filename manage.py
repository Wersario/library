import requests


url = 'http://tululu.org/txt.php?id=32168'
answer = requests.get(url)
answer.raise_for_status()

print(answer.text)
