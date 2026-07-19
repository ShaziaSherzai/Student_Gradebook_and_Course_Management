## Full Name: 
Shazia Sherzai
## Project Title 
Student Gradebook and Course Management
## Project Description
The student Gradebook and Course Management System is a Python Object_Oriented Programming (OOP) project that helps
manage students, courses, assessments, and grades. Users can add students and courses, enroll students in courses, 
create assessments, record grades, assign letter grades, and generate student reports. The system also allows searching 
and deleting students and adding teacher comments to student reports.
## How to run the project:
1. Open the Project in PyCharm or another Python IDE.
2. Make sure all project files are in the same folder. 
3. Run the main.py file.
4. Use the menu to:
- Add a student
- Add a course 
- Enroll a student in a course 
- Add assessments
- Record Grades
- Calculate averages 
- Add teacher comments
- View student reports 
- Search students
- Delete Students
- Exit the program

## Classes created
- The project contains the following classes:
### Student
- Stores student information such as student ID, name, email, and enrolled courses. 
### Courses 
- Stores course information, enrolled students, and assessments.
### Assessments 
- Parent class for all assessments. 
- Store assessment title and maximum score. 
- Calculates percentages and displays assessment information.
### Quiz
- Inherits from the assessment class.
### Exam  
Inherits from the assessment class.
### Project 
Inherits from the assessment class.
### Gradebook
- Manages students, courses, enrollments, grades, averages, reports, searching, deleting students, and teacher comments. 
## Object-Oriented Programming Concepts
### Encapsulation
Encapsulation is used in the student class through getter and setter methods:
- get_id()
- get_name()
- set_email()
The email is updated only after validation, protecting the object's data.
### Inheritance
Inheritance is used by creating specialized assessment classes:
- Quiz → Assessment 
- Exam → Assessment 
- Project → Assessment 
These classes inherit common attributes and methods from the Assessment class.
### Method Overriding 
Method overriding is used in the child classes by providing their own versions of: 
- display_info()
- grade_message()
Each assessment type displays its own information and grading message. 
### Custom Features
### 1. Letter Grade
The system converts a student's average percentage into a letter grade. 
### 2. Teacher Comments 
Teachers can add personalized comments for each student. The comments are displayed in the student's report to provide 
feedback on performance. 
