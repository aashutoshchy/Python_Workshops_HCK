n = int(input("Enter a number: "))
orgNum = n

rev = 0

while n != 0:
    r = n % 10
    rev = (rev * 10) + r
    n = n // 10

print("Reverse is: ", rev)

if rev == orgNum:
    print("It is Palindrome.")
else:
    print("It is not Palindrome.")


