import math


def annual_payment():
    p = float(input("pls, enter summ of the credit "))
    i = float(input("pls, enter the interest rate "))
    n = float(input("pls, enter the amount of payments "))
    ii = i / (12 * 100)
    annualpayment = p * (ii * math.pow(1 + ii, n) / (math.pow(1 + ii, n) - 1))
    annul = math.ceil(annualpayment)
    print(f"your monthly payment = {annul}!")


def loan_principle():
    a = float(input("pls, enter the annual payment "))
    i = float(input("pls, enter the interest rate "))
    n = float(input("pls, enter the amount of payments "))
    ii = i / (12 * 100)
    loanprinciple = a / ((ii * math.pow(1 + ii, n)) / (math.pow(1 + ii, n) - 1))
    loanprin = math.ceil(loanprinciple)
    print(f"your loan principle = {loanprin}!")


def number_of_payments():
    p = float(input("pls, enter summ of the credit "))
    a = float(input("pls, enter the annunity monthly payment "))
    i = float(input("pls, enter the loan interest rate "))
    ii = i / (12 * 100)
    n = math.log(a / (a - (ii * p)), 1 + ii)
    months = math.ceil(n % 12)
    years = math.floor(n / 12)

    if n < 12:
        print(f"it will takes {months} months")
    elif n > 12:
        print(f"it will takes {years} years and {months} months")


def diff():
    principal = int(input("Enter the loan principal:"))
    periods = int(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))
    i = interest / (12 * 100)
    overpayment = 0
    for m in range(1, periods + 1):
        differ = math.ceil((principal / periods) + i * (principal - ((principal * (m - 1)) / periods)))
        print(f"Month {m}: payment is {differ}")
        overpayment = overpayment + differ
        continue
    print(f"Overpayment = {overpayment - principal}")


def start():
    select = int(input("""What do you want to calculate?
type "1" for number of monthly payments,
type "2" for annuity monthly payment amount,
type "3" for loan principal: 
type "4" for diff: """))
    if select == 1:
        number_of_payments()
    elif select == 2:
        annual_payment()
    elif select == 3:
        loan_principle()
    elif select == 4:
        diff()
    else:
        print("try again")
        start()


start()
