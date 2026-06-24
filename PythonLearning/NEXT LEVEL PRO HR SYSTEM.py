class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.salary}"

def save_employee(e):
    f = open("employees.txt", "a")
    f.write(str(e) + "\n")
    f.close()
def load_employees():
    employees = []

    try:
        f = open("employees.txt", "r")

        for line in f:
            emp_id, name, salary = line.strip().split(",")
            e = Employee(emp_id, name, int(salary))
            employees.append(e)

        f.close()
    except:
        pass

    return employees
def add_employee():
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    employees = load_employees()

    emp_id = len(employees) + 1

    e = Employee(emp_id, name, salary)
    save_employee(e)

    print("Employee Added with ID:", emp_id)

def show_employees():
    employees = load_employees()

    for e in employees:
        print(e.emp_id, e.name, e.salary)


def search_employee():
    employees = load_employees()

    key = input("Enter ID or Name: ")

    found = False

    for e in employees:
        if key == str(e.emp_id) or key.lower() in e.name.lower():
            print("Found:", e.emp_id, e.name, e.salary)
            found = True

    if not found:
        print("Not Found")


def delete_employee():
    employees = load_employees()

    emp_id = input("Enter ID to delete: ")

    employees = [e for e in employees if str(e.emp_id) != emp_id]

    f = open("employees.txt", "w")
    for e in employees:
        f.write(str(e) + "\n")
    f.close()

    print("Deleted Successfully")

while True:
    print("\n--- PRO HR SYSTEM ---")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        show_employees()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        delete_employee()

    elif choice == 5:
        break