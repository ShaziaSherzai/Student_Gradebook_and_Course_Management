class Gradebook:
    def __init__(self, passing_grade = 55):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = passing_grade

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_course(self, course):
        self.courses[course.course_code] = course

    def enroll_students(self, students_id, course_code):
        if students_id in self.students and course_code in self.courses:
            if students_id not in self.grades:
                self.grade[students_id] = {}
            self.grades[students_id][course_code] = {}
        else:
            print("Students or course not found")

    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].assessments.append(assessment)

    def record_grade(self, students_id, course_code, assessment_title, score):
        if students_id in self.students and course_code in self.courses and assessment_title in self.courses[course_code].assessments:
            self.grades[students_id][course_code][assessment_title] = score

    def calculate_average(self, students_id, course_code):
        scores = self.grades.get(students_id, {}).get(course_code, {})
        return sum(scores) / len(scores) if scores else 0

    def get_result(self, average):
        return "Passed" if average >= self.passing_grade else "Failed"

    def show_report(self, student_id):
        if student_id not in self.students:
            print("Student not found")
            return
        student = self.students[student_id]
        print(f"Report for {student.student_id}")
        for course_code, assessments in self.grades.get(student_id, {}).items():
            avg = self.calculate_average(student_id, course_code)
            result = self.get_result(avg)
            print(f"course: {self.courses[course_code].course_name}")
            print(f"Grades: {assessments}")
            print(f"Average: {avg:.2f} {result}")

    def search_student(self, keyword):
        for student_id, student in self.students.items():
            if keyword.lower() in student_id or keyword.lower() in student.name.lower():
                return student
            return None

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            if student_id in self.grades:
                del self.grades[student_id]