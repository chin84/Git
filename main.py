class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rate = float()

        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rate = float()

    def __str__(self):

        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for marks in self.grades:
            grades_count += len(self.grades[marks])
        self.average_rate = sum(map(sum, self.grades.values())) / grades_count
        result = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rate}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return result

    def rate_lectors_grade(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Данные неверны!'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('УПС...Так нельзя!!')
            return
        return self.average_rate < other.average_rate


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):

        self.average_rate = float()
        self.grades = {}
        self.name = name
        self.surname = surname
        self.courses_attached = []

        super().__init__(name, surname)
        self.average_rate = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for marks in self.grades:
            grades_count += len(self.grades[marks])
        self.average_rate = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('УПС...Так нельзя!!')
            return
        return self.average_rate < other.average_rate


class Reviewer(Mentor):
    def rate_lectors_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Данные неверны!'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


best_lector_first = Lecturer('Феоктист', 'Волгодонский')
best_lector_first.courses_attached += ['Python']

best_lector_second = Lecturer('Корнелий', 'Бабочкин')
best_lector_second.courses_attached += ['C++']

best_lector_third = Lecturer('Севастьян', 'Вишниевксий')
best_lector_third.courses_attached += ['Python']


first_reviewer = Reviewer('Дармидонт', 'Скабичевский')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['C++']

second_reviewer = Reviewer('Мифодий', 'Вареников')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['C++']

first_student = Student('Протас', 'Кириешкин')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['HTML CSS']

second_student = Student('Илларион', 'Краснознаменский')
second_student.courses_in_progress += ['C++']
second_student.finished_courses += ['HTML CSS']

third_student = Student('Святополк', 'Мечевой')
third_student.courses_in_progress += ['Python']
third_student.finished_courses += ['HTML CSS']

first_student.rate_lectors_grade(best_lector_first, 'Python', 10)
first_student.rate_lectors_grade(best_lector_first, 'Python', 10)
first_student.rate_lectors_grade(best_lector_first, 'Python', 10)

first_student.rate_lectors_grade(best_lector_second, 'Python', 5)
first_student.rate_lectors_grade(best_lector_second, 'Python', 7)
first_student.rate_lectors_grade(best_lector_second, 'Python', 8)

first_student.rate_lectors_grade(best_lector_first, 'Python', 7)
first_student.rate_lectors_grade(best_lector_first, 'Python', 8)
first_student.rate_lectors_grade(best_lector_first, 'Python', 9)

second_student.rate_lectors_grade(best_lector_second, 'C++', 10)
second_student.rate_lectors_grade(best_lector_second, 'C++', 8)
second_student.rate_lectors_grade(best_lector_second, 'C++', 9)

third_student.rate_lectors_grade(best_lector_third, 'Python', 5)
third_student.rate_lectors_grade(best_lector_third, 'Python', 6)
third_student.rate_lectors_grade(best_lector_third, 'Python', 7)

first_reviewer.rate_lectors_grade(first_student, 'Python', 8)
first_reviewer.rate_lectors_grade(first_student, 'Python', 9)
first_reviewer.rate_lectors_grade(first_student, 'Python', 10)

second_reviewer.rate_lectors_grade(second_student, 'C++', 8)
second_reviewer.rate_lectors_grade(second_student, 'C++', 7)
second_reviewer.rate_lectors_grade(second_student, 'C++', 9)

second_reviewer.rate_lectors_grade(third_student, 'Python', 9)
second_reviewer.rate_lectors_grade(third_student, 'Python', 9)
second_reviewer.rate_lectors_grade(third_student, 'Python', 9)
second_reviewer.rate_lectors_grade(third_student, 'Python', 9)
second_reviewer.rate_lectors_grade(third_student, 'Python', 9)
second_reviewer.rate_lectors_grade(third_student, 'Python', 9)

print(f'Перечень студентов:\n\n{first_student}\n\n{second_student}\n\n{third_student}')
print()
print()

print(f'Перечень лекторов:\n\n{best_lector_first}\n\n{best_lector_second}\n\n{best_lector_third}')
print()
print()

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{first_student.name} {first_student.surname} < {second_student.name} {second_student.surname} = {first_student > second_student}')
print()

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lector_first.name} {best_lector_first.surname} < {best_lector_second.name} {best_lector_second.surname} = {best_lector_first > best_lector_second}')
print()

students = [first_student, second_student, third_student]

lectors = [best_lector_first, best_lector_second, best_lector_third]

def student_rating(students, course_name):
    overal = 0
    overal_count = 0
    for stud in students:
       if stud.courses_in_progress == [course_name]:
            overal += stud.average_rate
            overal_count += 1
    average_rate = round(overal / overal_count,1)
    return round(average_rate,1)

def lecturer_rating(lectors, course_name):
    overal = 0
    overal_count = 0
    for lect in lectors:
        if lect.courses_attached == [course_name]:
            overal += lect.average_rate
            overal_count += 1
    average_rate = overal / overal_count
    return round(average_rate,1)

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(students, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lectors, 'Python')}")
print()