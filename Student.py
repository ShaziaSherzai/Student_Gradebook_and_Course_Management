class Student:
    def __init__(self, student_id, name, email, courses):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = courses

    def get_id(self):
        return self.student_id
    def get_name(self):
        return self.name
    def set_email(self, email):
        if "@" in email and "." in email:
            self.email = email
            print("Email updated successfully")
        else:
            print("Invalid email address")

    def enrol_course(self, course_code):
        self.courses.append(course_code)

    def display_info(self):
        print("student info")
        print("Student ID: ", self.student_id)
        print("Student Name: ", self.name)
        print("Student Email: ", self.email)
        print("Courses: ", self.courses)
        



