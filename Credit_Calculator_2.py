import math
import sys

def credit_type():
    P = 0
    A = 0
    n = 0
    i = 0

    for types in args:
        for j in range(len(types)):
            if types[j] == "=":
                if types[:j] == "--principal":
                    P = float(types[j+1:])

                elif types[:j] == "--payment":
                    A =float(types[j+1:])

                elif types[:j] == "--interest":
                    i = float(types[j+1:])/(12*100)

                elif types[:j] == "--periods":
                    n = int(types[j+1:])

    if P < 0 or A < 0 or i < 0 or n < 0:
        print("Incorrect parameters.")
    elif args[1] == "--type=annuity":
        if P != 0 and A != 0 and i != 0:
            return count_of_months(P, A, i)
        elif P != 0 and n != 0 and i != 0:
            return monthly_payment(P, n, i)
        elif A != 0 and n != 0 and i != 0:
            return credit_principal(A, n, i)
        elif A != 0 and n != 0 and A != 0:
            print("Incorrect parameters.")
    elif args[1] == "--type=diff":
        if A != 0:
            print("Incorrect parameters.")
        else:
            return differentiated_payment(P, n, i)


def count_of_months(P, A, i):
    n = math.ceil(math.log((A / (A - i * P)), (1 + i)))

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
    print(f"Overpayment = {(n * A - P):.0f}")

def monthly_payment(P, n, i):

    A = math.ceil(P * ((i * pow((1+i),n)) / (pow((1+i),n) - 1)))
    print(f"Your annuity payment = {A}!")
    print(f"Overpayment = {(n * A - P):.0f}")

def credit_principal(A, n, i):

    P = A / ((i * pow((1+i),n)) / (pow((1+i),n) - 1))

    print(f"Your credit principal = {P:.0f}!")
    print(f"Overpayment = {(n * A - P):.0f}")

def differentiated_payment(P, n, i):

    m = 1
    Dm_sum = 0
    while m <= n:
        Dm = math.ceil((P / n) + (i * (P - ((P * (m - 1)) / n))))
        print(f"Month {m}: paid out {Dm:.0f}")
        Dm_sum += Dm
        m += 1

    print(f"Overpayment = {(Dm_sum - P):.0f}")




args = sys.argv

if len(args) != 5:
    print("Incorrect parameters.")
elif args[1] != "--type=annuity":
    if args[1] == "--type=diff":
        credit_type()
    else:
        print("Incorrect parameters.")
elif args[1] != "--type=diff":
    if args[1] == "--type=annuity":
        credit_type()
    else:
        print("Incorrect parameters.")
else:
    credit_type()

