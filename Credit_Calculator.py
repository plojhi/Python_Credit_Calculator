import math

def count_of_months():
    print("Enter credit principal:")
    P = int(input("> "))

    print("Enter monthly payment:")
    A = float(input("> "))

    print("Enter credit interest:")
    i = (float(input("> ")) / 12) / 100

    n = math.log((A / (A - i * P)), (1 + i))

    if n // 12 == 1 and n % 12 == 0:
        print(f"You need {(n // 12):.0f} year to repay this credit!")
    elif n % 12 == 0 and n // 12 != 1:
        print(f"You need {(n // 12):.0f} years to repay this credit!")
    elif math.ceil(n % 12) == 12:
        print(f"You need {((n // 12)+1):.0f} years to repay this credit!")
    elif n // 12 == 0:
        print(f"You need {math.ceil(n % 12)} months to repay this credit!")
    else:
        print(f"You need {round(n // 12)} years and {math.ceil(n % 12)} months to repay this credit!")

def monthly_payment():
    print("Enter credit principal:")
    P = int(input("> "))

    print("Enter count of periods:")
    n = int(input("> "))

    print("Enter credit interest:")
    i = (float(input("> ")) / 12) / 100

    A = math.ceil(P * ((i * pow((1+i),n)) / (pow((1+i),n) - 1)))
    print(f"Your annuity payment = {A}!")

def credit_principal():
    print("Enter monthly payment:")
    A = float(input("> "))

    print("Enter count of periods:")
    n = int(input("> "))

    print("Enter credit interest:")
    i = (float(input("> ")) / 12) / 100

    P = A / ((i * pow((1+i),n)) / (pow((1+i),n) - 1))

    print(f"Your credit principal = {P:.0f}!")



print("What do you want to calculate?")
print('type "n" - for count of months,')
print('type "a" - for annuity monthly payment:')
print('type "p" - for credit principal:')
action = input("> ")

if action == "n":
    count_of_months()

elif action == "a":
    monthly_payment()

elif action == "p":
    credit_principal()
