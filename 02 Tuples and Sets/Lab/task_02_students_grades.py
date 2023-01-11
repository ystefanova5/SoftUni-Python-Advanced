students_count = int(input())
students = {}
for _ in range(students_count):
    student, grade = input().split()
    if student not in students:
        students[student] = []
    students[student].append(float(grade))
for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    student_grades = " ".join(f"{grade:.2f}" for grade in grades)
    print(f"{name} -> {student_grades} (avg: {average_grade:.2f})")


################################################   Task Description   ################################################
# 2. Students' Grades
# Write a program that reads students' names and their grades and adds them to the student record.
# On the first line, you will receive the number of students – N.
# On the following N lines, you will be receiving a student's name and grade.
# For each student print all his/her grades and finally his/her average grade,
# formatted to the second decimal point in the format:
# "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})"
# The order in which we print the result does not matter.
