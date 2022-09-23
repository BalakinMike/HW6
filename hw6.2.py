from audioop import avg
from statistics import mean
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        
        self.grades = {}
        self.avg_st = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)

        
    def rate_lecture(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in mentor.courses_attached and course in self.courses_in_progress:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            print(f'Ошибка. {mentor.name} {mentor.surname} не является лектором курса {course}')
            return 'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        for count in self.courses_in_progress:
            self.avg_st[count] = mean(self.grades[count]) # Словарь - хранитель среднего
            print(f'Средняя оценка за домашние задания {count}: ', mean(self.grades[count]))
        print(f'Курсы в процессе изучения: {self.courses_in_progress}')
        print(f'Завершенные курсы: {self.finished_courses}')
        return' '

    def __lt__(self, other):
        
        return self.avg_st < other.avg_st
    #    return self.avg_st['JS'] < other.avg_st['JS']  

    def __eq__(self, other):
        
        return self.avg_st == other.avg_st  


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
 
   

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.avg = {}
    
    
    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        for count in self.courses_attached:
            self.avg[self.surname] = mean(self.grades[count]) # Словарь - хранитель среднего
            print('Средняя оценка за лекции: ', self.avg[self.surname])
        return' '

    def __lt__(self, other):
        
        return self.avg[self.surname] < other.avg[other.surname]  

    def __eq__(self, other):
        
        return self.avg[self.surname] == other.avg[other.surname]   
    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        return ' '

def info_st(surname):
    if surname == student_1.surname:
        print(student_1)
    elif surname == student_2.surname:
        print(student_2)

def comparison_mentor():
    if mentor_1 == mentor_2:
        print(f'Балл {mentor_1.name} {mentor_1.surname} равен баллу {mentor_2.name} {mentor_2.surname}')
    else:
        print(f'Балл {mentor_1.name} {mentor_1.surname} меньше балла {mentor_2.name} {mentor_2.surname}' if mentor_1 < mentor_2 else f'Балл {mentor_1.name} {mentor_1.surname} больше балла {mentor_2.name} {mentor_2.surname}') #print(mentor_1.avg[mentor_1.surname]<mentor_2.avg[mentor_2.surname])



def comparison_st(course):
    if student_1.avg_st[course] == student_2.avg_st[course]:
        print(f'Балл {student_1.name} {student_1.surname} равен баллу {student_2.name} {student_2.surname}')
    else:
        print(f'Балл {student_1.name} {student_1.surname} меньше балла {student_2.name} {student_2.surname}' if student_1.avg_st[course] < student_2.avg_st[course] else f'Балл {student_1.name} {student_1.surname} больше балла {student_2.name} {student_2.surname}') 

def average_students():
    n = 0
    surname = ' '
    surnames = []
    ball = 0   
    while surname != '':
        surname = input('Введите фамилию студента: ')
        surnames += [surname]
    print(surnames)
    
    name_course = input('Введите название курса (JS, Python)')
    for count_s in surnames:
        if count_s in stunents_family:
            print (count_s)
    return
    #         ball += count_s.avg_st[name_course]
    #         n += 1
    # return (ball/n) 

surnames = []
stunents_family = []
# Идентификаторы студентов
student_1 = Student('Mike', 'Balakin', 'man')
student_1.courses_in_progress += ['Python', 'JS']
student_1.finished_courses += ['Git', 'Основы командной строки']
stunents_family += [student_1.surname]

student_2 = Student('Gena', 'Krocodail', 'Crocodail')
student_2.courses_in_progress += ['Python', 'JS']
student_2.finished_courses += ['HTML', 'Git']
stunents_family += [student_2.surname]

# Идентификаторы лекторов 
mentor_1 = Lecturer('Cerg', 'Vertepov')
mentor_1.courses_attached += ['JS']

mentor_2 = Lecturer('Alexander', 'Bardin')
mentor_2.courses_attached += ['Python']

# Идентификаторы проверяющих
mentor_3 = Reviewer('Evgeny', 'Varlamov')
mentor_3.courses_attached += ['JS']

mentor_4 = Reviewer('Igor', 'Chebotar')
mentor_4.courses_attached += ['Python']

# Оценки студентов за курс Python 
mentor_4.rate_hw(student_1, 'Python', 10)
mentor_4.rate_hw(student_1, 'Python', 9)
mentor_4.rate_hw(student_2, 'Python', 5)
mentor_4.rate_hw(student_2, 'Python', 4)

# Оценки студентов за курс JS
mentor_3.rate_hw(student_1, 'JS', 2)
mentor_3.rate_hw(student_1, 'JS', 8)
mentor_3.rate_hw(student_2, 'JS', 5)
mentor_3.rate_hw(student_2, 'JS', 10)

# Оценки лекторов за работу
student_1.rate_lecture(mentor_2, 'Python', 10) 
student_2.rate_lecture(mentor_2, 'Python', 7)
student_2.rate_lecture(mentor_1, 'JS', 7)
student_1.rate_lecture(mentor_1, 'JS', 2)



# Просто проверочный вывод (вне задания)
# print(student_1.grades)
# print(student_2.grades)
# print(f'Лектор {mentor_2.name} {mentor_2.surname} имеет баллы {mentor_2.grades}')
# print(f'Лектор {mentor_1.name} {mentor_1.surname} имеет баллы {mentor_1.grades}')
# print(f' Средние баллы {student_1.surname} за Python', student_1.avg_st['Python'])
# print(student_2.avg_st)

print('---------------------')
# Вывод информации по преподавателям
print(mentor_1)
print(mentor_2)
print(mentor_4)

print('---------------------')
# Вывод информации по студентам
print(student_1)
print(student_2)

info_s = input('Для вывода информации по конкретному студенту введите фамилию: ')
if info_s in stunents_family:
    info_st(info_s) 

comp_ment = input('Для сравнения баллов преподавателей введите Y или любую клавишу для отказа: ')
comp_ment = comp_ment.upper()
if comp_ment == 'Y':
    comparison_mentor()
    print(mentor_1.surname, mentor_1.avg[mentor_1.surname], mentor_2.surname, mentor_2.avg[mentor_2.surname])
course_stud = input('Для сравнения баллов студентов введите название курса (JS, Python) или любую клавишу для отказа: ')
if course_stud == 'JS' or course_stud == 'Python':
    comparison_st(course_stud)

average_students()
x = student_2
print(x.avg_st)