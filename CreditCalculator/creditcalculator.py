import math


def annual_payment_func():
    principal_credit_sum = float(input("pls, enter sum of the credit "))
    interest_rate = float(input("pls, enter the interest rate "))
    amount_of_payments = float(input("pls, enter the amount of payments "))
    nominal_rate_percents = interest_rate / (12 * 100)
    annual_payment = principal_credit_sum * (nominal_rate_percents *
                                             math.pow(1 + nominal_rate_percents, amount_of_payments)
                                             / (math.pow(1 + nominal_rate_percents, amount_of_payments) - 1))
    annual_ceil = math.ceil(annual_payment)
    print(f"your monthly payment = {annual_ceil}!")
    start()


def loan_principle_func():
    annual_payment = float(input("pls, enter the annual payment "))
    interest_rate = float(input("pls, enter the interest rate "))
    nominal_rate = float(input("pls, enter the amount of payments "))
    interest_rate_percents = interest_rate / (12 * 100)
    loan_principle = annual_payment / ((interest_rate_percents * math.pow(1 + interest_rate_percents, nominal_rate))
                                       / (math.pow(1 + interest_rate_percents, nominal_rate) - 1))
    loan_principle_ceil = math.ceil(loan_principle)
    print(f"your loan principle = {loan_principle_ceil}!")
    start()


def number_of_payments():
    principle_credit_sum = float(input("pls, enter sum of the credit "))
    annual_payment = float(input("pls, enter the annual monthly payment "))
    interest_rate = float(input("pls, enter the loan interest rate "))
    interest_rate_percents = interest_rate / (12 * 100)
    nominal_rate = math.log(annual_payment /
                            (annual_payment - (interest_rate_percents * principle_credit_sum)),
                            1 + interest_rate_percents)
    months = math.ceil(nominal_rate % 12)
    years = math.floor(nominal_rate / 12)

    if nominal_rate < 12:
        print(f"it will takes {months} months")
    elif nominal_rate > 12:
        print(f"it will takes {years} years and {months} months")
    start()


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
    start()


def start():
    select = int(input("""What do you want to calculate?
                        type "1" for number of monthly payments,
                        type "2" for annuity monthly payment amount,
                        type "3" for loan principal: 
                        type "4" for diff: """))
    if select == 1:
        number_of_payments()
    elif select == 2:
        annual_payment_func()
    elif select == 3:
        loan_principle_func()
    elif select == 4:
        diff()
    else:
        print("try again")
        start()


start()
