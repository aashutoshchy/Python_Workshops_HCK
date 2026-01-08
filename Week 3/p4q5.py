"""
Accept the age and gender, number of days and displays the wages accordingly
"""

age = int(input("Enter age: "))
gen = input("Enter gender (m/f): ")

wage = 0

if 18 <= age < 30:
    if gen == 'm':
        wage = 700
    else:
        wage = 750

elif 30 <= age <= 40:
    if gen == 'm':
        wage = 800
    else:
        wage = 850

print("Wage is: ", wage)
