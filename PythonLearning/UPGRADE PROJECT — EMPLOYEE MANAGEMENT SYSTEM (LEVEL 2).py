class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def status(self):
        if self.salary >= 3000:
            return "PASS"
        else:
            return "FAIL"
employees = []
n = int(input("How many employees? "))

for i in range(n):
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    e = Employee(name, salary)
    employees.append(e)

for e in employees:
    print(e.name, e.salary, e.status())

print("Total Employees:", len(employees))
