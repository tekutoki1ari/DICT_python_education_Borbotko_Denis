import requests
from bs4 import BeautifulSoup

url = input("Enter the URl:\n> ")
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
if 'imdb.com' not in url or 'title' not in url:
    print("Invalid quote resource!")
elif r.status_code != 200:
    print("Invalid quote resource!")
else:
    soup = BeautifulSoup(r.content, "lxml")

    title = soup.find('title')
    split_title = title.text.split(sep=" ")
    w = 0
    for item in split_title:
        if "(" in item:
            w = split_title.index(item)

    description = soup.find('meta', {'name': 'description'})
    result = {'title': ' '.join(split_title[0:w]), 'description': description['content']}
    print(result)
