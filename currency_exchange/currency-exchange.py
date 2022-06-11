while True:
    try:
        my_coins = float(input("Please, enter the number of mycoins you have:\n> "))
        e_rate = float(input("Please, enter the exchange rate:\n> "))
        break
    except ValueError:
        print("\nInvalid input, write only numbers\n")

result = e_rate * my_coins
print(f'The total amount of dollars: {result}')