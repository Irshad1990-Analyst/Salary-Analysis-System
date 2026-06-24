class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.salary}"


def save_all(employees):
    f = open("employees.txt", "w")
    for e in employees:
        f.write(str(e) + "\n")
    f.close()


def load_employees():
    employees = []

    try:
        f = open("employees.txt", "r")

        for line in f:
            emp_id, name, salary = line.strip().split(",")
            employees.append(Employee(emp_id, name, int(salary)))

        f.close()
    except:
        pass

    return employees


def add_employee():
    employees = load_employees()

    emp_id = len(employees) + 1
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    employees.append(Employee(emp_id, name, salary))
    save_all(employees)

    print("Employee Added")


def show_employees():
    employees = load_employees()

    for e in employees:
        print(e.emp_id, e.name, e.salary)


def search_employee():
    employees = load_employees()

    key = input("Enter ID or Name: ")

    for e in employees:
        if key == str(e.emp_id) or key.lower() in e.name.lower():
            print("Found:", e.emp_id, e.name, e.salary)


def delete_employee():
    employees = load_employees()

    emp_id = input("Enter ID to delete: ")

    employees = [e for e in employees if str(e.emp_id) != emp_id]

    save_all(employees)

    print("Deleted Successfully")


while True:
    print("\n--- PRO HR SYSTEM ---")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        show_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        break