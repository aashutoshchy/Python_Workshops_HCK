userChoice = 'y'
ans = 0

while userChoice.lower() != 'q':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        ans = num1 + num2
    elif operation == '-':
        ans = num1 - num2
    elif operation == '*':
        ans = num1 * num2
    elif operation == '/':
        ans = num1 / num2
    else:
        print("Please enter correct operation")
        continue

    print(f"{num1} {operation} {num2} = {ans}")
    userChoice = input("Do you want to continue? Press 'q' to stop: ")
