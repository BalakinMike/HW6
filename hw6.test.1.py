class Student:
    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.cours_in_progress = []
        self.finished_course = []
        self.grades = {}
        

    def lectors_grades (self, lector, course, grade: int):
        
        if (isinstance(lector, Lector) and course in lector.courses and course in self.cours_in_progress):
            if course in lector.grades:
                lector.grades[course].append(grade)
            else:
                lector.grades[course] = [grade]
    
    def avg_grade (self):
        balls = [item for grade in self.grades.values() for item in grade]
        avg_balls = sum(balls)/len(balls) 
        return avg_balls

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\nКурсы в процессе изучения: {self.cours_in_progress}' \
                f'\nЗавершённые курсы: {self.finished_course}\nСредний балл за домашние работы: {self.avg_grade()}'

    def __lt__(self, other):

class Mentor:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses = []

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lector(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}
    
    def avg_grade (self):
        balls = [item for grade in self.grades.values() for item in grade]
        avg_balls = sum(balls)/len(balls) 
        return avg_balls
    
    def __str__(self) -> str:
        return Mentor.__str__(self) + f'\nСредний балл за лекции: {self.avg_grade()}'

class Reviewer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses = []
    
    def students_grades (self, student, course, grade: int):
        if (isinstance(student, Student) and course in student.cours_in_progress):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
    


student_1 = Student(name='Mikhail', surname='Balakin', gender='Male')
student_2 = Student(name='Gena', surname='Krocodail', gender='Crocodail')

student_1.cours_in_progress += ['HTML', 'Python']
student_2.cours_in_progress += ['HTML', 'Python']
student_1.finished_course += ['Git', 'JS']
student_2.finished_course += ['Git', 'JS']


lector_1 = Lector(name='Alexander', surname='Bardin')
lector_2 = Lector(name='Sergey', surname='Vertepov')

lector_1.courses += ['Python']
lector_2.courses += ['HTML']

reviewer_3 = Reviewer(name='Evgeny', surname='Varlamov')
reviewer_4 = Reviewer(name='Igor', surname='Chebotar')

reviewer_3.students_grades(student_1, 'Python', 10)
reviewer_3.students_grades(student_2, 'Python', 7)
reviewer_4.students_grades(student_1, 'HTML', 6)
reviewer_4.students_grades(student_2, 'HTML', 5)
# Ввод второй оценки за курсы
reviewer_3.students_grades(student_1, 'Python', 9)
reviewer_3.students_grades(student_2, 'Python', 8)
reviewer_4.students_grades(student_1, 'HTML', 7)
reviewer_4.students_grades(student_2, 'HTML', 7)

student_1.lectors_grades(lector_1,'Python', 10)
student_2.lectors_grades(lector_1,'Python', 7)
student_1.lectors_grades(lector_2,'HTML', 7)
student_2.lectors_grades(lector_2,'HTML', 5)

# Тестовые выводы
print('-'*10)
print('Студенты:')
print(student_1)
print(student_2)

print('-'*10)
print('Лекторы:')
print(lector_1)
print(lector_2)

print('-'*10)
print('Проверяющие:')
print(reviewer_3)
print(reviewer_4)

print('-'*10)
print(student_1.grades)