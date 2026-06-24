class Employee:
    def __init__(self):
        self.__salary = 5000

    def get_salary(self):
        return self.__salary

e = Employee()

print(e.get_salary())