class Employee:
    pass
e1 = Employee()
e1.name = "Irshad"
e1.salary = 5000
print(e1.name)
print(e1.salary)

class Employee:
    def show(self):
        print(self.name , self.salary)

e1 = Employee()
e1.name = "Irshad"
e1.salary = 5000

e1.show()

class Employee:
    def show(self):
        print("Hello")

e = Employee()
e.show()

class Employee:
    def __init__(self, name):
        self.name = name

e1 = Employee("Irshad")
e2 = Employee("Ahmed")

print(e1.name)
print(e2.name)

class Employee:
    company = "TCS"   # class variable

    def __init__(self, name):
        self.name = name

e1 = Employee("Irshad")
e2 = Employee("Ahmed")

print(e1.company)
print(e2.company)


class Employee:
    company = "ABC"

    def __init__(self, name):
        self.name = name

e1 = Employee("Irshad")
e2 = Employee("Ahmed")

print(e1.company, e1.name)
print(e2.company, e2.name)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def check(self):
        if self.salary >= 3000:
            return "PASS"
        else:
            return "FAIL"


employees = [
    ("Irshad", 3000),
    ("Ahmed", 2000),
    ("Salim", 4000)
]

for name, salary in employees:
    emp = Employee(name, salary)
    print(name, emp.check())


class Employee:
    def __init__(self, name):
        self.name = name

employees = ["A", "B"]

for name in employees:
    e = Employee(name)
    print(e.name)

class Employee:
    def __init__(self, name):
        self.name = name


employees = {
    "A": "Irshad",
    "B": "Ahmed"
}

for key in employees:
    e = Employee(employees[key])
    print(e.name)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def check_status(self):
        if self.salary >= 3000:
            return "PASS"
        else:
            return "FAIL"


employees = {
    "A": ("Irshad", 3000),
    "B": ("Ahmed", 2000),
    "C": ("Salim", 4000)
}

for key in employees:
    name, salary = employees[key]

    e = Employee(name, salary)

    print(e.name, e.check_status())