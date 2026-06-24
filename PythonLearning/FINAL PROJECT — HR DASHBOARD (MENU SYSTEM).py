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
while True:
    print("\n--- HR DASHBOARD ---")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Highest Salary")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        salary = int(input("Enter salary: "))

        e = Employee(name, salary)
        employees.append(e)
        print("Employee Added!")
    elif choice == 2:
        for e in employees:
            print(e.name, e.salary, e.status())
    elif choice == 3:
            name = input("Enter name to search: ")

            found = False
            for e in employees:
                if e.name == name:
                    print(e.name, e.salary, e.status())
                    found = True

            if not found:
                print("Employee Not Found")
    elif choice == 4:
        name = input("Enter name to update: ")

        for e in employees:
            if e.name == name:
                new_salary = int(input("Enter new salary: "))
                e.update_salary(new_salary)
                print("Salary Updated!")
    elif choice == 5:
        highest = employees[0]

        for e in employees:
            if e.salary > highest.salary:
                highest = e

        print("Highest Salary Employee:")
        print(highest.name, highest.salary)
    elif choice == 6:
        print("Exiting System...")
        break
