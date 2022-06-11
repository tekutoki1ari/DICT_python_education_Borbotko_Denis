import requests

url = input("Enter the URl:\n> ")
r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
if r.status_code != 200:
    print(f'The URL returned {r.status_code}!')
else:
    page = requests.get(url).content
    file = open("source.html", "wb+")
    file.write(page)
    file.close()
    print('Content saved!')