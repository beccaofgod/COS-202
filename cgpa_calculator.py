print("========================================")
print("PERSONAL POCKET CGPA CALCULATOR")
print("========================================")

total_grade_point = float(input("Enter Total Grade Point: "))
total_credit_unit = float(input("Enter Total Credit Unit: "))

cgpa = total_grade_point / total_credit_unit

print("CGPA =", cgpa)

if cgpa >= 4.50 and cgpa <= 5.00:
    print("Class of Degree: First Class")

elif cgpa >= 3.50 and cgpa <= 4.49:
    print("Class of Degree: Second Class Upper")

elif cgpa >= 2.40 and cgpa <= 3.49:
    print("Class of Degree: Second Class Lower")

elif cgpa >= 1.50 and cgpa <= 2.39:
    print("Class of Degree: Third Class")

elif cgpa >= 1.00 and cgpa <= 1.49:
    print("Class of Degree: Pass")

else:
    print("Class of Degree: Fail")