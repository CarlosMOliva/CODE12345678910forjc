students = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

class_total = 0
count = 0

for student in range(1, students + 1):
    print(f"Student {student}")
    student_total = 0

    for subject in range(1, subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        student_total += score
        class_total += score
        count += 1

    student_average = student_total / subjects
    print(f"Average for student {student} = {student_average}")

class_average = class_total / count
print(f"Class average = {class_average}")
