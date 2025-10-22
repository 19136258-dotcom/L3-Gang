#ask the user for their exam score
#print the grade based on the score
examscore = int(input("Enter your exam score (0-100): "))
if examscore >= 90 and examscore <= 100:
    print("Grade: A")
elif examscore >= 80 and examscore < 90:
    print("Grade: B")
elif examscore >= 70 and examscore < 80:
    print("Grade: C")
elif examscore >= 60 and examscore < 70:
    print("Grade: D")
elif examscore < 60:
    print("Grade: Fail")
else:
    print("Invalid score. Please enter a score between 0 and 100.")
