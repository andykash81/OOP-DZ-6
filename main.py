from classes import Student, Lecturer, Reviewer


def average_rating_st(name, courses):
    a_r = 0
    for item in range(len(student_list)):
        for course in student_list[item].courses_in_progress:
            if (name == student_list[item].name) and (courses == course):
                a_r = sum(student_list[item].grades[courses]) / len(student_list[item].grades[courses])
            else:
                return
    return a_r


def average_rating_lec(name, courses):
    a_r = 0
    for item in range(len(lecturer_list)):
        for course in lecturer_list[item].courses_attached:
            if (name == lecturer_list[item].name) and (courses == course):
                a_r = sum(lecturer_list[item].grades[course]) / len(lecturer_list[item].grades[course])
            else:
                return
    return a_r


def rating_st(name):
    rating = 0
    sum_value = 0
    len_value = 0
    for i in range(len(student_list)):
        if name == student_list[i].name:
            for value in student_list[i].grades.values():
                sum_value += sum(value)
                len_value += len(value)
            rating = sum_value / len_value
    return rating


def rating_lec(name):
    rating = 0
    sum_value = 0
    len_value = 0
    for i in range(len(lecturer_list)):
        if name == lecturer_list[i].name:
            for value in lecturer_list[i].grades.values():
                sum_value += sum(value)
                len_value += len(value)
            rating = sum_value / len_value
    return rating


if __name__ == '__main__':
    student_list = []
    lecturer_list = []
    reviewer_list = []
    name_student1 = Student('Roy', 'Eman', 'your_gender')
    name_student1.courses_in_progress += ['Python']
    name_student1.courses_in_progress += ['Git']
    name_student1.finished_courses += ['Введение в программирование']

    name_student2 = Student('Bob', 'Hone', 'your_gender')
    name_student2.courses_in_progress += ['Python']
    name_student2.courses_in_progress += ['Git']
    name_student2.finished_courses += ['Английский для программистов']

    name_lector1 = Lecturer('Some', 'Buddy')
    name_lector1.courses_attached += ['Python']
    name_lector1.courses_attached += ['Git']

    name_lector2 = Lecturer('Katy', 'May')
    name_lector2.courses_attached += ['Python']
    name_lector2.courses_attached += ['Git']

    name_reviewer1 = Reviewer('Tom', 'Smith')
    name_reviewer1.courses_attached += ['Python']
    name_reviewer1.courses_attached += ['Git']

    name_reviewer2 = Reviewer('Sam', 'Kits')
    name_reviewer2.courses_attached += ['Python']
    name_reviewer2.courses_attached += ['Git']

    name_student1.grad_lector(name_lector1, 'Python', 10)
    name_student1.grad_lector(name_lector1, 'Git', 8)
    name_student2.grad_lector(name_lector1, 'Python', 7)
    name_student2.grad_lector(name_lector1, 'Git', 9)

    name_student1.grad_lector(name_lector2, 'Python', 9)
    name_student1.grad_lector(name_lector2, 'Git', 10)
    name_student2.grad_lector(name_lector2, 'Python', 8)
    name_student2.grad_lector(name_lector2, 'Git', 6)

    name_reviewer1.grade_student(name_student1, 'Python', 6)
    name_reviewer1.grade_student(name_student1, 'Python', 8)
    name_reviewer1.grade_student(name_student1, 'Python', 10)
    name_reviewer1.grade_student(name_student1, 'Git', 10)
    name_reviewer1.grade_student(name_student1, 'Git', 7)

    name_reviewer2.grade_student(name_student2, 'Python', 9)
    name_reviewer2.grade_student(name_student2, 'Python', 7)
    name_reviewer2.grade_student(name_student2, 'Python', 10)
    name_reviewer2.grade_student(name_student2, 'Git', 10)
    name_reviewer2.grade_student(name_student2, 'Git', 6)

    student_list.append(name_student1)
    student_list.append(name_student2)

    lecturer_list.append(name_lector1)
    lecturer_list.append(name_lector2)

    reviewer_list.append(name_reviewer1)
    reviewer_list.append(name_reviewer2)

    name_student1.average_rating['Python'] = average_rating_st(name_student1.name, 'Python')
    name_student1.average_rating['Git'] = average_rating_st(name_student1.name, 'Git')

    name_lector1.average_rating['Python'] = average_rating_lec(name_lector1.name, 'Python')
    name_lector1.average_rating['Git'] = average_rating_lec(name_lector1.name, 'Git')

    name_lector2.average_rating['Python'] = average_rating_lec(name_lector2.name, 'Python')
    name_lector2.average_rating['Git'] = average_rating_lec(name_lector2.name, 'Git')

    name_student1.rating = rating_st(name_student1.name)
    name_student2.rating = rating_st(name_student2.name)

    name_lector1.rating = rating_lec(name_lector1.name)
    name_lector2.rating = rating_lec(name_lector2.name)

    print(name_student1)
    print(name_student2)
    print(name_lector1)
    print(name_lector2)
    print(name_reviewer1)
    print(name_reviewer2)

    if name_student1.rating > name_student2.rating:
        print(f'Рейтинг студента {name_student1.surname} {name_student1.name} выше рейтинга студента '
              f'{name_student2.surname} {name_student2.name}')
    else:
        print(f'Рейтинг студента {name_student1.surname} {name_student1.name} ниже рейтинга студента '
              f'{name_student2.surname} {name_student2.name}')

    if name_lector1.rating > name_lector2.rating:
        print(f'Рейтинг преподавателя {name_lector1.surname} {name_lector1.name} выше рейтинга преподавателя '
              f'{name_lector2.surname} {name_lector2.name}')
    else:
        print(f'Рейтинг преподавателя {name_lector1.surname} {name_lector1.name} ниже рейтинга преподавателя '
              f'{name_lector2.surname} {name_lector2.name}')
