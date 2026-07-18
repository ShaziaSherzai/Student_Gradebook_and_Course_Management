from Student import Student
from Course import Course
from Quiz import Quiz
from Exam import Exam
from Project import Project
from Assessment import Assessment
from Gradebook import Gradebook

gradebook = Gradebook()

while True:
    print("\n============Student Gradebook and Course Management==========")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Add Assessment")
    print("5. Record student grade")
    print("6. calculate Student Average")
    print("7. Show Student Report")
    print("0. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        student_id = int(input("Enter student ID: "))
        name = input("Student Name: ")
        email = input("Email Address: ")
        student = Student(student_id, name, email, [])
        gradebook.add_student(student)
        print("Student Added Successfully!")

    elif choice == 2:
        course_code = input("Course Code: ")
        course_name = input("Course Name: ")
        course = Course(course_code, course_name)
        gradebook.add_course(course)
        print("Course Added Successfully!")


