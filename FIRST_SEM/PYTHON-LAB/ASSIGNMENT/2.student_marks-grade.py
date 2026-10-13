mark1 = float(input("Enter marks for Subject I: "))
mark2 = float(input("Enter marks for Subject II: "))
mark3 = float(input("Enter marks for Subject III: "))
if (mark1 < 0 or mark1 > 100 or
    mark2 < 0 or mark2 > 100 or
    mark3 < 0 or mark3 > 100):
    
    print("Invalid marks! Marks must be between 0 and 100.")

else:
    total = mark1 + mark2 + mark3
    average = total / 3
    percentage = (total / 300) * 100 

    if percentage >= 70:
        grade = "DISTINCTION"
    elif percentage >= 60:
        grade = "FIRST CLASS"
    elif percentage >= 40:
        grade = "SECOND CLASS"
    else:
        grade = "FAIL"

    print("Total      :", total)
    print("Average    :", average)
    print("Percentage :", percentage)
    print("Grade      :", grade)