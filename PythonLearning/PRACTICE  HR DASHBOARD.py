class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

employees = []
def add_employee():
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    e = Employee(name,salary)
    employees.append(e)

def show_employees():
    for e in employees:
        print(e.name)
        print(e.salary)

def search_employee():
    name = input("Enter name: ")

    for e in employees:
        if e.name == name:
            print(e.name, e.salary)
            return

    print("Not Found")
while True:
    print("1 Add")
    print("2 Show")
    print("3 Search")
    print("4 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        show_employees()

    elif choice == 3:
        search_employee()

    elif choice == 4:
        break