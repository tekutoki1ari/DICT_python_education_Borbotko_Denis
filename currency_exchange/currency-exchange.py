KZT = 1.234
GBP = 23.05
EUR = 0.21
ARS = 2.7891

while True:
    try:
        MyC = float(input("Please, enter the number mycoins you have:\n> "))
        break
    except ValueError:
        print("\nInvalid input, write only numbers\n")

KZT_r = MyC * KZT
GBP_r = MyC * GBP
EUR_r = MyC * EUR
ARS_r = MyC * ARS

print(f'''I will get {round(KZT_r, 2)} KZT from the sale of {MyC} mycoins.
I will get {round(GBP_r, 2)} GBP from the sale of {MyC} mycoins.
I will get {round(EUR_r, 2)} EUR from the sale of {MyC} mycoins.
I will get {round(ARS_r, 2)} ARS from the sale of {MyC} mycoins.''')
