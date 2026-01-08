# a
user_input = input("Enter either 'A', 'B' or 'C' \n> ").upper()

if user_input in ('A', 'B', 'C'):
    if user_input == 'A':
        print("Apple")
    elif user_input == 'B':
        print("Banana")
    else:
        print("Cat")

else:
    print("Invalid Input")
    