def calc_grade():
    asg1 = int(input("Enter your score in English: "))
    asg2 = int(input("Enter your score in Nepali: "))
    asg3 = int(input("Enter your score in Math: "))
    asg4 = int(input("Enter your score in Computer Science: "))
    asg5 = int(input("Enter your score in Accounting: "))

    if (asg1 > 100 or asg2 > 100 or asg3 > 100 or asg4 > 100 or asg5 > 100):
        print("Enter your correct mark!")
        return

    total_score = asg1 + asg2 + asg3 + asg4 + asg5
    total_perc = (total_score / 500) * 100

    print(f"Total Percentage is {total_perc}%")


calc_grade()
