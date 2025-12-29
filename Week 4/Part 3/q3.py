# a

# total = 0

# for i in range(100, 201, 1):
#     if i%2==0:
#         total += i

# print("total is: ", total)

#b

# total = 0
# userChoice = 'Y'

# while userChoice == 'Y':
#     n = int(input("Enter a number: "))

#     if n <= 100:
#         total += n

#     userChoice = input("Do You Want to Continue?(Y/N): ")

# print("Sum is:", total)


#c
# c

total = 0
i = 100

while True:
    if i > 200:
        break

    if i % 2 != 0:
        i += 1
        continue

    total += i
    i += 1

print("Sum is:", total)

