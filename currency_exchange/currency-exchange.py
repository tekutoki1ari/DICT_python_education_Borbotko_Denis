import requests

while True:
    try:
        ur_code = input("Enter your currency code:\n> ").lower()
        request = requests.get(f'http://www.floatrates.com/daily/{ur_code}.json').json()
        break
    except ValueError:
        print("\nNon-existent currency code, try again.\n")

cash = dict()

if ur_code != 'usd':
    cash['usd'] = request['usd']['rate']
if ur_code != 'eur':
    cash['eur'] = request['eur']['rate']

while True:

    while True:
        try:
            desired_code = input('Enter desired currency code or "exit":\n> ').lower()
            if desired_code not in request.keys() and desired_code != "exit" and desired_code != ur_code:
                raise ValueError
            break
        except ValueError:
            print("\nNon-existent currency code, try again.\n")
    if desired_code == "exit":
        break

    while True:
        try:
            money = float(input("Enter the amount of money:\n> "))
            break
        except ValueError:
            print("\nInvalid input, please enter only numbers\n")

    if desired_code == ur_code:
        print(f"\nHmm.. You received {money}\n")
    elif desired_code in cash.keys():
        print("\nChecking the cache...\nIt is in the cache!")
        print(f'You received {round(money * cash[f"{desired_code}"], 2)}\n')
    elif desired_code not in cash.keys():
        print(f'\nChecking the cache...\nSorry, but it is not in the cache!')
        cash[f'{desired_code}'] = request[f'{desired_code}']['rate']
        print(f'You received {round(money * cash[f"{desired_code}"], 2)}\n')