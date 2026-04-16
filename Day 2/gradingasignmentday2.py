print("Enter your GPA:")
gpa = float(input())
if gpa > 4.0 and gpa < 0.0:
    print("Invalid GPA. GPA must be between 0 and 4.")
elif gpa >= 3.6 and gpa <= 4:
    print("Your GPA is A+")
elif gpa >= 3.2 and gpa <= 3.6:
    print("Your GPA is A")
elif gpa >= 2.8 and gpa <= 3.2:
    print("Your GPA is B+")
elif gpa >= 2.4 and gpa <= 2.8:
    print("Your GPA is B")
elif gpa >= 2.0 and gpa <= 2.4:
    print("Your GPA is C+")
elif gpa >= 1.6 and gpa <= 2.0:
    print("Your GPA is C")
elif gpa >= 0.0 and gpa <= 1.6:
    print("You got NG")
else:
    print("Please enter a valid GPA")
