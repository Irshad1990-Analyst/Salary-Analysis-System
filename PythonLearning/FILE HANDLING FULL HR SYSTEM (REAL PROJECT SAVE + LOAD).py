class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def status(self):
        if self.salary >= 3000:
            return "PASS"
        else:
            return "FAIL"

    def __str__(self):
        return f"{self.name},{self.salary}"

def save_employee(emp):
    f = open("employees.txt", "a")
    f.write(str(emp) + "\n")
    f.close()

def load_employees():
    employees = []

    f = open("employees.txt", "r")

    for line in f:
        name, salary = line.strip().split(",")
        e = Employee(name, int(salary))
        employees.append(e)

    f.close()
    return employees
def add_employee():
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    e = Employee(name, salary)
    save_employee(e)

    print("Employee Saved!")
def show_employees():
    employees = load_employees()

    for e in employees:
        print(e.name, e.salary, e.status())
def search_employee():
    employees = load_employees()

    name = input("Enter name to search: ")
    found = False

    for e in employees:
        if e.name == name:
            print(e.name, e.salary, e.status())
            found = True

    if not found:
        print("Employee Not Found")
employees = []

while True:
    print("\n--- HR DASHBOARD ---")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        show_employees()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        break