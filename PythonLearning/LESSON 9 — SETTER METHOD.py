class Employee:
    def __init__(self):
        self.__salary = 3000

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


e = Employee()

e.set_salary(5000)

print(e.get_salary())

class Student:
    def __init__(self):
        self.__mark = 50

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

s = Student()

s.set_mark(80)

print(s.get_mark())