def calculate():
    oper = input('ENTER AN OPERATOR')
    x = int(input('ENTER A NUMBER'))
    y = int(input('ENTER SECOND NUMBER'))

    if oper == '+':
        print("{} + {} = ".format(x, y))
        print(x + y)

    elif oper == "-":
        print("{} - {} = ".format(x, y))
        print(x - y)

    elif oper == "x":
        print("{} x {} = ".format(x, y))
        print(x * y)

    elif oper == "/":
        print("{} / {} = ".format(x, y))
        print(x / y)

    else:
        calculate()
    again()

def again():
    a = input('''WOULD YOU 
    LIKE TO CALCULATE AGAIN?
    Y / N''')

    if a.upper == "Y":
        calculate()

    elif a.upper == "N":
        print('see ya layter')

    else:
        print('PLEASE TYPE IN A VALID ANSWER')
        again()
