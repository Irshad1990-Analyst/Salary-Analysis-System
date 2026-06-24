class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def status(self):
        if self.salary >= 3000:
            return "PASS"
        else:
            return "FAIL"

employees = {
    "E1": ("Irshad", 3500),
    "E2": ("Ahmed", 2000),
    "E3": ("Salim", 4000)
}

for key in employees:
    name, salary = employees[key]
    e = Employee(name, salary)
    print(e.name, e.status())

    


