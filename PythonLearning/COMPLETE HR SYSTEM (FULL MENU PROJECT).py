import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*",
    database="HR_DB"
)

cursor = conn.cursor()


def add_employee():
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))

    sql = "INSERT INTO employees (id, name, salary) VALUES (%s, %s, %s)"
    val = (emp_id, name, salary)

    cursor.execute(sql, val)
    conn.commit()
    print("Employee Added")


def show_employees():
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)


def search_employee():
    name = input("Enter Name: ")
    sql = "SELECT * FROM employees WHERE name = %s"
    cursor.execute(sql, (name,))
    for row in cursor.fetchall():
        print(row)


def update_employee():
    emp_id = int(input("Enter ID: "))
    salary = int(input("New Salary: "))

    sql = "UPDATE employees SET salary = %s WHERE id = %s"
    cursor.execute(sql, (salary, emp_id))
    conn.commit()
    print("Updated")


def delete_employee():
    emp_id = int(input("Enter ID: "))

    sql = "DELETE FROM employees WHERE id = %s"
    cursor.execute(sql, (emp_id,))
    conn.commit()
    print("Deleted")


while True:
    print("\n--- HR SYSTEM MENU ---")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        show_employees()
    elif choice == 3:
        search_employee()
    elif choice == 4:
        update_employee()
    elif choice == 5:
        delete_employee()
    elif choice == 6:
        break