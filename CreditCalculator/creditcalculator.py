creditsum = int(input("pls, enter the summ of ur credit "))


def monthly_payment():
    global creditsum
    months = int(input("pls, enter amount of months "))
    payment = creditsum / months
    lastpayment = creditsum - (months - 1) * payment
    if payment == lastpayment:
        print(f"ur monthly payment is {round(payment)}")
    elif payment != lastpayment:
        print(f"ur monthly payment is {round(payment)} and the lastone is {lastpayment}")

def last_payment():
    global creditsum
    monthlypayment = int(input("pls, enter the monthly payment "))
    amount_months = creditsum / monthlypayment
    print(f"it will take {round(amount_months)} months to repay the loan")


def start():
    Start = int(input("""what u want to calculate
1 - number of monthly payments
2 - for the monthly payment"""))
    if Start == 1:
        last_payment()
    elif Start == 2:
        monthly_payment()
    else:
        print("try again")
        start()

start()
