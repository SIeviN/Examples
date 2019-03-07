# A = P ((r(1+r)^n) / (1+r)^n - 1)

# P = principal
# A = periodic amortization payment
# r = periodic interest rate divided by 100 (also divided by 12 in case of monthly installments)
# n = total number of monthly payments


def amortization(principal, interest, years):


    interRatePP = ((interest/100)/12)
    numPayments = years*12
    numer = (interRatePP * (1 + interRatePP)**numPayments)
    denom = (((1 + interRatePP)**numPayments) - 1)

    monthlyPayment = principal * (numer / denom)
    totInterest = (monthlyPayment * numPayments) - principal
    total = monthlyPayment * 12 * years

    print("Your monthly payment would be ${:.2f} for {} years and you would pay ${:.2f} in interest.".format(monthlyPayment, years, totInterest))

    f = open("amortization.txt", "w+")
    while total >= 0:
        f.write("Total: ${:.2f}\n".format(total))
        total -= monthlyPayment
        if total <= 0:
            f.write("Total: $0\nPaid off\nCongratulations")

    # numPayments = (years-10) * 12
    # numer = (interRatePP * (1 + interRatePP)**numPayments)
    # denom = (((1 + interRatePP)**numPayments) - 1)
    # monthlyPayment = principal * (numer / denom)
    # totInterest -= ((monthlyPayment * numPayments) - principal)

    # print("At the same rate, if you were to pay ${:.2f} a month, you would pay off the loan 10 years faster and save ${:.2f} in interest".format(monthlyPayment, totInterest))
    f.close()

if __name__ == "__main__":
    print("30-year loan amortization calculator")
    print("Enter your loan amount (numbers only)")
    principal = float(input())
    print("Enter your interest rate (%)")
    interest = float(input())

    amortization(principal, interest, 30)

