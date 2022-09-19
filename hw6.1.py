class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    ...

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

student_1 = Student('Mike', 'Balakin', 'man')
student_1.courses_in_progress += ['Python', 'JS']

student_2 = Student('Gena', 'Krocodail', 'Crocodail')
student_2.courses_in_progress += ['Python', 'JS']
 
mentor_1 = Lecturer('Cerg', 'Vertepov')
mentor_1.courses_attached += ['JS']

mentor_2 = Lecturer('Alexander', 'Bardin')
mentor_2.courses_attached += ['Python']

mentor_3 = Reviewer('Evgeny', 'Varlamov')
mentor_3.courses_attached += ['JS']

mentor_4 = Reviewer('Igor', 'Chebotar')
mentor_4.courses_attached += ['Python']
 
mentor_4.rate_hw(student_1, 'Python', 10)
mentor_4.rate_hw(student_2, 'Python', 5)

mentor_3.rate_hw(student_1, 'JS', 10)
mentor_3.rate_hw(student_2, 'JS', 5)

 
print(student_1.grades)
print(student_2.grades)