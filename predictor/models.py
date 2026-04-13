class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

class StudentGrade:
    def __init__(self, student_id, course_code, grade):
        self.student_id = student_id
        self.course_code = course_code
        self.grade = grade

class Prediction:
    def __init__(self, student_id, predicted_grade):
        self.student_id = student_id
        self.predicted_grade = predicted_grade
