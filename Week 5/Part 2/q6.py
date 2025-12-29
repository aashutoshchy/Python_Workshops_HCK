
list = []
num = input("Enter a number to add to the list: ")
while num != "0":
    temp = int(num)
    if temp > 100:
        list.append("over")
    else:
        list.append(temp)
    num = input("Enter a number to add to the list and enter 0 to stop adding: ")
print (list)