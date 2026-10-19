print("STUDENT MARKS CALCULATOR")
print("Enter marks out of 100 for each subject.")

name = input("Enter your name: ")

ict = float(input("Enter ICT marks: "))
dld = float(input("Enter DLD marks: "))
dsa = float(input("Enter DSA marks: "))

if ict < 0 or ict > 100 or dld < 0 or dld > 100 or dsa < 0 or dsa > 100:
    print("Invalid marks! Each mark must be between 0 and 100.")
else:
    total = ict + dld + dsa
    percentage = (total / 300) * 100

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\nRESULT")
    print("Student name:", name)
    print("Total marks:", total, "out of 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)