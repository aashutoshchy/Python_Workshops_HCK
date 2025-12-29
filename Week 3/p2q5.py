per1 = int(input("Enter the age of first person: "));
per2 = int(input("Enter the age of second person: "));
per3 = int(input("Enter the age of third person: "));
per4 = int(input("Enter the age of fourth person: "));

if per1>per2 and per1>per3 and per1>per4:
    print("The oldest person is ", per1);
elif per2>per1 and per2>per3 and per2>per4:
    print("The oldest person is ", per2);
elif per3>per1 and per3>per2 and per3>per4:
    print("The oldest person is ", per3);

else:
    print("The oldest person is ", per4);
    
