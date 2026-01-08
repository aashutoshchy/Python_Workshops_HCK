MP = int(input("Enter marked price: "))

if MP > 10000:
    discount = 20
elif 7000 < MP <= 10000:
    discount = 15
else:
    discount = 10

net_amt = MP - (discount/100*MP)
print("Your Price is: ", net_amt)
