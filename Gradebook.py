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

    def enroll_students(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            if student_id not in self.grades:
                self.grades[student_id] = {}
            if course_code not in self.grades[student_id]:
                self.grades[student_id][course_code] = {}

            self.students[student_id].enrol_course(course_code)
            self.courses[course_code].add_student(student_id)
            print("Student enrolled successfully!")
        else:
            print("Students or course not found.")

    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].assessments.append(assessment)

    def record_grade(self, students_id, course_code, assessment_title, score):
        if students_id not in self.students:
            print("Student not found")
            return
        if course_code not in self.courses:
            print("Course not found")
            return
        assessment = self.courses[course_code].find_assessments(assessment_title)
        if assessment is None:
            print("Assessment not found")
            return
        self.grades[students_id][course_code][assessment_title] = score
        print("Grade recorded successfully!")

    def calculate_average(self, students_id, course_code):
        grades = self.grades.get(students_id, {}).get(course_code, {})
        if not grades:
            return 0
        total_percentage = 0
        count = 0

        for assessment in self.courses[course_code].assessments:
            if assessment.title in grades:
                score = grades[assessment.title]
                percentage = score / assessment.max_score * 100
                total_percentage += percentage
                count += 1

        if count == 0:
            return 0
        return total_percentage / count



    def get_result(self, average):
        return "Passed" if average >= self.passing_grade else "Failed"

    def get_letter_grade(self, average):
        if average >= 95:
            return "A+"
        elif average >= 90:
            return "A"
        elif average >= 85:
            return "B+"
        elif average >= 80:
            return "B"
        elif average >= 75:
            return "C+"
        elif average >= 70:
            return "C"
        elif average >= 65:
            return "D+"
        elif average >= 60:
            return "D"
        else:
            return "F"


    def show_report(self, student_id):
        if student_id not in self.students:
            print("Student not found")
            return
        student = self.students[student_id]
        print("\n=======Student report========")
        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Email: {student.email}")

        for course_code, grades in self.grades.get(student_id, {}).items():
            course = self.courses[course_code]

            print(f"\ncourse: {course.course_code}")
            print(f"\ngrades: ")

            for assessment in course.assessments:
                if assessment.title in grades:
                    score = grades[assessment.title]
                    percentage = score / assessment.max_score * 100

                    print(f"{assessment.title}: {score}/{assessment.max_score} = {percentage:.0f}%")

            average = self.calculate_average(student_id, course_code)
            result = self.get_result(average)
            letter_grade = self.get_letter_grade(average)

            print(f"\nAverage: {average:.2f}%")
            print(f"Letter grade: {letter_grade}")
            print(f"result: {result}")

    def search_student(self, keyword):
       keyword = keyword.lower()
       for student_id, student in self.students.items():
            if (keyword in student_id.lower() or
                    keyword in student.name.lower()):
                return student
       return None

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            if student_id in self.grades:
                del self.grades[student_id]

            for course in self.courses.values():
                if student_id in course.students:
                    course.students.remove(student_id)