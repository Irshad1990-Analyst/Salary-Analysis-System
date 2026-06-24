import os

employees = []

# 🔥 LOAD when program starts
def load_data():
    global employees
    employees = []

    if os.path.exists("employees.txt"):
        f = open("employees.txt", "r")

        for line in f:
            id, name, salary = line.strip().split(",")

            employees.append({
                "id": int(id),
                "name": name,
                "salary": int(salary)
            })

        f.close()


# 🔥 SAVE automatically
def save_data():
    f = open("employees.txt", "w")

    for e in employees:
        f.write(f'{e["id"]},{e["name"]},{e["salary"]}\n')

    f.close()


# 🔥 ADD
def add_employee():
    emp_id = len(employees) + 1
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    employees.append({"id": emp_id, "name": name, "salary": salary})

    save_data()   # AUTO SAVE


# 🔥 SHOW
def show():
    for e in employees:
        print(e)


# 🔥 SEARCH
def search():
    key = input("Enter ID or Name: ")

    for e in employees:
        if key == str(e["id"]) or key.lower() in e["name"].lower():
            print("Found:", e)


# 🔥 DELETE
def delete():
    global employees
    emp_id = input("Enter ID: ")

    employees = [e for e in employees if str(e["id"]) != emp_id]

    save_data()   # AUTO SAVE


# 🔥 PROGRAM START
load_data()

while True:
    print("\n1.Add 2.Show 3.Search 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        show()

    elif choice == "3":
        search()

    elif choice == "4":
        delete()

    elif choice == "5":
        break