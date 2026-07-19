from Student import Student
from Course import Course
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
    print("7. Add Teacher Comment")
    print("8. Show Student Report")
    print("9. Search Student")
    print("10. Delete Student")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        student_id = input("Enter student ID: ").strip()
        name = input("Student Name: ").strip()
        email = input("Email Address: ").strip()
        student = Student(student_id, name, email, [])
        gradebook.add_student(student)
        print("Student Added Successfully!")

    elif choice == "2":
        course_code = input("Course Code: ")
        course_name = input("Course Name: ")
        course = Course(course_code, course_name, [], [])
        gradebook.add_course(course)
        print("Course Added Successfully!")

    elif choice == "3":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        gradebook.enroll_students(student_id, course_code)


    elif choice == "4":
        course_code = input("Course Code: ")
        title = input("Assessment Title: ")
        max_score = int(input("Maximum Score: "))
        assessment = Assessment(title, max_score)
        gradebook.add_assessment(course_code, assessment)
        print("Assessment Added Successfully!")

    elif choice == "5":
        student_id = input("Student ID: ").strip()
        course_code = input("Course Code: ").strip()
        assessment_title = input("Assessment Title: ").strip()

        while True:
            try:
                score = float(input("score: "))
                break
            except ValueError:
                print("Invalid score. Please try again.")

        gradebook.record_grade(student_id, course_code, assessment_title, score)

    elif choice == "6":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        average = gradebook.calculate_average(student_id, course_code)
        print(f"\nAverage Percentage: {average:.2f}%")
        print("Result:", gradebook.get_result(average))

    elif choice == "7":
        student_id = input("Student ID:")
        comment = input("Teacher Comment: ")
        gradebook.add_teacher_comment(student_id, comment)

    elif choice == "8":
        student_id = input("Student ID: ")
        gradebook.show_report(student_id)

    elif choice == "9":
        keyword = input("Enter Student ID or Name: ")
        student = gradebook.search_student(keyword)
        if student:
            print("\nStudent Found")
            student.display_info()
        else:
            print("\nStudent Not Found")

    elif choice == "10":
        student_id = input("Enter student ID to delete: ")

        if student_id in gradebook.students:
            gradebook.delete_student(student_id)
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found")

    elif choice == "0":
        print("System Closed. Thank you😊")
        break

    else:
        print("Invalid choice! please try again.")





