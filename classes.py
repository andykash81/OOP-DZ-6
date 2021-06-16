class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = {}
        self.rating = 0

    def grad_lector(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        prt = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:' \
              f' {self.rating}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return prt

    def __lt__(self, another_student):
        if not isinstance(another_student, Student):
            print('Не является студентом')
            return
        return self.rating > another_student.rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = {}
        self.rating = 0

    def __str__(self):
        prt = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.rating}'
        return prt

    def __lt__(self, another_lecturer):
        if not isinstance(another_lecturer, Lecturer):
            print('Не является студентом')
            return
        return self.rating > another_lecturer.rating


class Reviewer(Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        prt = f'Имя: {self.name}\nФамилия: {self.surname}'
        return prt

    def grade_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
