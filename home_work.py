from abc import ABC, abstractmethod

class University:
    def __init__(self, name, address):
        self._name = name
        self._address = address
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def remove_department(self, department):
        self._departments.remove(department)

    def find_department(self, name):
        for department in self._departments:
            if department.get_name() == name:
                return department
        return None

class Department:
    def __init__(self, name, code, head):
        self._name = name
        self._code = code
        self._head = head

    def get_name(self):
        return self._name

    def get_head(self):
        return self._head

class Professor:
    def __init__(self, name, expertise):
        self._name = name
        self._expertise = expertise

    def get_name(self):
        return self._name

    def get_department(self):
        return self._department

class Student:
    def __init__(self, name, student_id, major):
        self._name = name
        self._student_id = student_id
        self._major = major
        self._courses = []

    def get_name(self):
        return self._name

    def get_major(self):
        return self._major

    def enroll_course(self, course):
        self._courses.append(course)

    def drop_course(self, course):
        self._courses.remove(course)

class Course:
    def __init__(self, name, code):
        self._name = name
        self._code = code

    def get_name(self):
        return self._name

# Створюємо університет
university = University("Назва університету", "Адреса університету")

# Створюємо відділення
department1 = Department("Відділення 1", "Код 1", Professor("Професор 1", "Експертиза 1"))
department2 = Department("Відділення 2", "Код 2", Professor("Професор 2", "Експертиза 2"))

# Додаємо відділення до університету
university.add_department(department1)
university.add_department(department2)

# Створюємо студента
student1 = Student("Студент 1", "ID1", "Спеціальність 1")
student2 = Student("Студент 2", "ID2", "Спеціальність 2")

# Записуємо студента на курс
course1 = Course("Курс 1", "Код 1")
course2 = Course("Курс 2", "Код 2")
student1.enroll_course(course1)
student2.enroll_course(course2)

# Виводимо інформацію про студента
print(f"Студент 1: {student1.get_name()}, Спеціальність: {student1.get_major()}")
print(f"Курси студента 1: {[course.get_name() for course in student1._courses]}")

# Виводимо інформацію про відділення
print(f"Відділення 1: {department1.get_name()}, Код: {department1._code}")
print(f"Керівник відділення 1: {department1.get_head().get_name()}, Експертиза: {department1.get_head()._expertise}")

# Виводимо інформацію про університет
print(f"Університет: {university._name}, Адреса: {university._address}")
