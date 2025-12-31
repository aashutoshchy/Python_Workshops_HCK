def calculator():     
    '''
    Create a Python program called calculator with functions to perform the following arithmetic calculations, each
    should take two decimal parameters and return the result of the arithmetic calculation in question.

        A) Addition B) Subtraction C) Multiplication
        D) Division E) Modulus F) Exponentiation
    '''


    help(calculator)

    firstNum = int(input("Enter firstNum: "))
    secNum = int(input("Enter secNum: "))
    operations = input("Enter your operations(+, -, *, /, %): ")

    if operations == '+':
        sum(firstNum, secNum)
    if operations == '-':
        diff(firstNum, secNum)
    if operations == '*':
        prod(firstNum, secNum)
    if operations == '/':
        div(firstNum, secNum)
    if operations == '%':
        mod(firstNum, secNum)

def sum(firstNum, secNum):
    print("Sum is: ", firstNum + secNum)

def diff(firstNum, secNum):
    print("Difference is: ", firstNum - secNum)

def prod(firstNum, secNum):
    print("Product is: ", firstNum * secNum)

def div(firstNum, secNum):
    print("Division is: ", firstNum / secNum)

def mod(firstNum, secNum):
    print("Modulus is: ", firstNum % secNum)

calculator()

