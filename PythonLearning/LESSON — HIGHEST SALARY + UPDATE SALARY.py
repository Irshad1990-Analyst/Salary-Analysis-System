class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def status(self):
        if self.salary >= 3000:
            return "PASS"
        else:
            return "FAIL"

    def update_salary(self, new_salary):
        self.salary = new_salary

employees = []

n = int(input("How many employees? "))

for i in range(n):
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    e = Employee(name, salary)
    employees.append(e)

for e in employees:
    print(e.name, e.salary, e.status())

highest = employees[0]

for e in employees:
    if e.salary > highest.salary:
        highest = e

print("Highest Salary Employee:")
print(highest.name, highest.salary)

name_to_update = input("Enter name to update salary: ")

for e in employees:
    if e.name == name_to_update:
        new_salary = int(input("Enter new salary: "))
        e.update_salary(new_salary)
        print("Salary Updated!")

