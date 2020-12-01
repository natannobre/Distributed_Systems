value = float(input())
firstTax = 0.00
secondTax = 0.00
thirdTax = 0.00

if value < 2000:
    print("Isento")
else: # if value is bigger than 2000, then it enters here
    if value < 3000:
        firstTax = value - 2000
    elif value < 4500:
        firstTax = 1000
        secondTax = value - 3000
    else:
        firstTax = 1000
        secondTax = 1500
        thirdTax = value - 4500

    print("R$ " + "{:.2f}".format(firstTax*0.08 + secondTax*0.18 + thirdTax*0.28))
    
