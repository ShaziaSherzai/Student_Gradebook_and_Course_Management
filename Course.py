class Course:
    def __init__(self, course_code, course_name, students, assignments):
        self.course_code = course_code
        self.course_name = course_name
        self.students = students
        self.assignments = assignments

    def add_student(self, student_id):
        self.students.append(student_id)

    def add_assessment(self, assessment):
        self.assignments.append(assessment)

    def find_assignments(self, title):
        for assessment in self.assessments:
            if assessment.title == title:
                return assessment
        return None

    def display_info(self):
        print(f"course code: {self.course_code}")
        print(f"course name: {self.course_name}")
        print(f"students: {len(self.students)}")
        print(f"assignments: {len(self.assignments)}")
