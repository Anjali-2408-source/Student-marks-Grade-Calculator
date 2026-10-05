# Student Marks & Grade Calculator

print("===== Student Marks & Grade Calculator =====")

name = input("Enter student name: ")

subjects = ["Python", "Mathematics", "Computer Science", "English", "Database"]

marks = []

for subject in subjects:
    mark = float(input(f"Enter marks in {subject} (out of 100): "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(subjects)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if percentage >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")