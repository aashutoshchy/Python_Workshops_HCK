# Create a function that prompts the user for two integer values and displays the results of the first number divided by the second to two decimal places.
def help():
    '''
    Creating a function that prompts the user for two integer values and displays the results of the first number
    divided by the second to two decimal places
    '''

def divide_two_numbers():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")

divide_two_numbers()
help()