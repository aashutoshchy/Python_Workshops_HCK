
weight = float(input("Enter your weight: "));
height = float(input("Enter your height: "));

bmi = weight/height**2

print(bmi)


if bmi < 18.5:
    print("Underweight");
elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight")
elif bmi >- 25 and bmi < 30:
    print("Overweight");
elif bmi >=30:
    print("obese");
else:
    print("Enter correct height and weight");
