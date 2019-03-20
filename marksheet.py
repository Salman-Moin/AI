computer = int(input("Computer Marks: "))
math = int(input("Math Marks: "))
physics = int(input("Physics Marks: "))
chemistry = int(input("Chemistry Marks: "))
english = int(input("English Marks: "))
total_marks = computer + math + physics + chemistry + english
percent = (total_marks / 500) * 100

if percent >= 80:
    grade = "A+"
elif percent >= 70:
    grade = "A"
elif percent >= 60:
    grade = "B"
elif percent >= 50:
    grade = "C"
elif percent >= 40:
    grade = "D"
else:
    grade = "Fail"
print("\nMarks Obtained: " + str(total_marks) + "\n" + "Percent: " + str(percent) + "\n" + "Grade: " + str(grade))