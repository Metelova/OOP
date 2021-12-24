class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectors(self, lecturer, course,grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress \
            and 0 < grade <= 10:
            lecturer.grades.append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        output = f'Имя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за дз: {average_rating(self.grades)} \
        \nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses }'
        return output

    def __it__(self, any_students):
        if isinstance(any_students, Student):
            return average_rating(self.grades) < average_rating(any_students.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# класс эксперт
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

# класс лекторы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_attached = []

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_rating(self.grades)}'
        return output

    def __it__(self, any_lecturer):
        if isinstance(any_lecturer, Lecturer):
            return average_rating(self.grades) < average_rating(any_lecturer.grades)

#Оценка студентов
def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
    else:
        return 'Ошибка'

#функция средней оценки
def average_rating(all_grades):
    if type(all_grades) is dict:
        amount_grades = []
        for grades in all_grades.values():
            for grade in grades:
                amount_grades.append(grade)
        return average_rating(amount_grades)
    elif type(all_grades) is list and all_grades[0] != None:
        average = round(sum(all_grades)/len(all_grades), 2)
        return average

#средняя оценка студентов по курсу
def average_course_grade(students,course):
    course_grade = []
    for student in students:
        if course in student.grades.keys():
            for any_grade in student.grades.get(course):
                course_grade.append(any_grade)
    return average_rating(course_grade)

#средняя оценка лекторов по курсам
def average_lecturer_grade(lecturers,course):
    lecturer_grade = []
    for lecturer in lecturers:
        for any_grade in lecturer.grades:
            lecturer_grade.append(any_grade)
    return average_rating(lecturer_grade)


#экзэмпляры класса
student_1 = Student("Ruoy", "Eman", 18)
student_1.courses_in_progress += ["Python"]
student_1.courses_in_progress += ["GIT"]
student_1.finished_courses +=["Введение в программирование"]
student_1.grades["Python"] = [10, 10, 10, 10, 10, 8]
student_2 = Student("Who", "IS", 31)
student_2.courses_in_progress += ["Python"]
student_2.finished_courses +=["GIT"]
student_2.grades["Python"] = [7, 10, 10, 5, 2, 8]
student_2.grades["GIT"] = [7, 10, 10, 5, 10, 8]

student_list = [student_1, student_2]

lecturer_1 = Lecturer("Some", "Body")
lecturer_1.courses_attached += ["Python"]
lecturer_1.grades = [10, 10, 10, 7]
lecturer_2 = Lecturer("Some2", "body2")
lecturer_2.courses_attached += ["Python"]
lecturer_2.grades = [10, 10, 10, 9]

lecturer_list = [lecturer_1,lecturer_2]

reviewer_1 = Reviewer("John ", "Doe")
reviewer_1.courses_attached = ["GIT"]
reviewer_2 = Reviewer("John2 ", "Doe2")
reviewer_2.courses_attached = ["Python"]

reviewer_list = [reviewer_1, reviewer_2]

#Печать средней оценки студентов и лекторов за курс
print(average_course_grade(student_list,"Python"))
print(average_lecturer_grade(lecturer_list, "Python"))

#печать классов
print(reviewer_1)
print(lecturer_1)
print(student_1)
