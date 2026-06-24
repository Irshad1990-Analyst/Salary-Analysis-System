employees = []

def add_employee():
    emp_id = len(employees) + 1
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    employee = {"id": emp_id, "name": name, "salary": salary}
    employees.append(employee)

def show_employees():
    for e in employees:
        print(e["id"], e["name"], e["salary"])


def search_employee():
    key = input("Enter ID or Name: ")

    for e in employees:
        if key == str(e["id"]) or key.lower() in e["name"].lower():
            print("Found:", e)

def delete_employee():
    global employees
    emp_id = input("Enter ID to delete: ")

    employees = [e for e in employees if str(e["id"]) != emp_id]


while True:
    print("\n1.Add 2.Show 3.Search 4.Delete 5.Exit")
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