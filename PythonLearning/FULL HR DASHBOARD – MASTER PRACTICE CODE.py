class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name},{self.salary}"


# =========================
# 💾 SAVE SINGLE EMPLOYEE
# =========================
def save_employee(e):
    f = open("employees.txt", "a")
    f.write(str(e) + "\n")
    f.close()

# =========================
# 📥 LOAD ALL EMPLOYEES
# =========================
def load_employees():
    employees = []

    try:
        f = open("employees.txt", "r")

        for line in f:
            name, salary = line.strip().split(",")
            e = Employee(name, int(salary))
            employees.append(e)

        f.close()

    except:
        pass

    return employees


# =========================
# ➕ ADD EMPLOYEE
# =========================
def add_employee():
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    e = Employee(name, salary)
    save_employee(e)

    print("Employee Added!")


# =========================
# 📋 SHOW (SORT BY SALARY)
# =========================
def show_employees():
    employees = load_employees()

    employees.sort(key=lambda e: e.salary, reverse=True)

    for e in employees:
        print(e.name, e.salary)


# =========================
# 🔍 SEARCH (CASE + PARTIAL)
# =========================
def search_employee():
    employees = load_employees()

    key = input("Enter name to search: ")

    found = False

    for e in employees:
        if key.lower() in e.name.lower():
            print("Found:", e.name, e.salary)
            found = True

    if not found:
        print("Not Found")


# =========================
# ❌ DELETE EMPLOYEE
# =========================
def delete_employee():
    employees = load_employees()

    name = input("Enter name to delete: ")

    employees = [e for e in employees if e.name.lower() != name.lower()]

    f = open("employees.txt", "w")
    for e in employees:
        f.write(str(e) + "\n")
    f.close()

    print("Deleted Successfully!")


# =========================
# 🔁 MENU LOOP
# =========================
while True:
    print("\n--- HR DASHBOARD ---")
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
        print("System Closed")
        break

