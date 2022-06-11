import requests

URL = input("Input the URL:\n> ")
r = requests.get(f'{URL}')
if r.status_code != 200:
    print("Invalid quote resource!")
else:
    print(r.json()["content"])
