class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def __str__(self):
        text = (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.get_average_grade()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n')

        if self.finished_courses:
            text += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return text

    def get_average_grade(self):
        all_grade = []
        for course_grades in self.grades.values():
            for course_grade in course_grades:
                all_grade.append(course_grade)
        return round(sum(all_grade) / len(all_grade), 1) if all_grade else 'Нет оценок'

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()

    def __eq__(self, other):
        return self.get_average_grade() == other.get_average_grade()

    def __ne__(self, other):
        return self.get_average_grade() != other.get_average_grade()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.get_average_grade()}\n')

    def get_average_grade(self):
        all_grade = []
        for course_grades in self.grades.values():
            for course_grade in course_grades:
                all_grade.append(course_grade)
        return round(sum(all_grade) / len(all_grade), 1) if all_grade else 'Нет оценок'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка добавления оценки')
            return 'Ошибка'


def get_avg_grade_students(students, courses):
    grade_list = []
    non_grade_list = []
    students_list = []
    for student in students:
        if isinstance(student, Student):
            students_list.append(student.name + ' ' + student.surname)
            for course in courses:
                if course in student.grades.keys():
                    grade_list += [grade for grade in student.grades[course]]
                else:
                    non_grade_list.append(course)
            if non_grade_list:
                return (f'Не удалось вычислить среднюю оценку домашних заданий: '
                        f'у студента {student.name} {student.surname} за курс(ы) '
                        f'{', '.join(non_grade_list)} нет оценок')
        else:
            return f'Нет такого студента'
    return (f'Средняя оценка домашних заданий студентов {', '.join(students_list)}'
            f' за курсы {', '.join(courses)}: {sum(grade_list) / len(grade_list)}')


def get_avg_grade_lecturers(lecturers, courses):
    grade_list = []
    non_grade_list = []
    lecturers_list = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            lecturers_list.append(lecturer.name + ' ' + lecturer.surname)
            for course in courses:
                if course in lecturer.grades.keys():
                    grade_list += [grade for grade in lecturer.grades[course]]
                else:
                    non_grade_list.append(course)
            if non_grade_list:
                return (f'Не удалось вычислить среднюю оценку лекций: '
                        f'у лектора {lecturer.name} {lecturer.surname} за курс(ы) '
                        f'{', '.join(non_grade_list)} нет оценок')
        else:
            return f'Нет такого лектора'
    return (f'Средняя оценка выступлений лекторов {', '.join(lecturers_list)}'
            f' на курсах {', '.join(courses)}: {sum(grade_list) / len(grade_list)}')


student1 = Student('Иван', 'Иванов', 'M')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student2 = Student('Петр', 'Петров', 'Ж')
student2.courses_in_progress = ['Python', 'Git', 'Введение в программирование']

lecturer1 = Lecturer('Альберт', 'Эйнштейн')
lecturer1.courses_attached = ['Python', 'Git']
lecturer2 = Lecturer('Не', 'Знайка')
lecturer2.courses_attached = ['Python', 'Git', 'Введение в программирование']


reviewer1 = Reviewer('Василий', 'Васильев')
reviewer1.courses_attached = ['Python', 'Git']
reviewer2 = Reviewer('Фома', 'Фомин')
reviewer2.courses_attached = ['Python', 'Введение в программирование']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 3)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Введение в программирование', 10)
reviewer2.rate_hw(student2, 'Python', 8)

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer2, 'Python', 3)
student1.rate_lecture(lecturer2, 'Введение в программирование', 10)

print(reviewer1)
print(lecturer1)
print(student1)

print(get_avg_grade_students([student1], ['Python', 'Git']))
print(get_avg_grade_students([student2], ['Введение в программирование']))
print(get_avg_grade_students([student1, student2], ['Python', 'Git']))
print(get_avg_grade_students([student1, student2], ['Python']))

print()
print(get_avg_grade_lecturers([lecturer1, lecturer2], ['Python']))
