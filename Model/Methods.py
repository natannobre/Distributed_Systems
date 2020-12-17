# AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER

def Calculator(num1, op, num2):
    num2 = float(num2)
    result = float(0)
    num1 = float(num1)

    if op == '+':
        result = num1 + num2

    elif op == '-':
        result = num1 - num2

    elif op == '*':
        result = num1 * num2

    elif op == '/':
        result = num1 / num2

    return result
