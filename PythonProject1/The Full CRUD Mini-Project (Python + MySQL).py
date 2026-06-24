import mysql.connector

# Database Connection
db = mysql.connector.connect(host="localhost", user="root", password="Irshad1990*", database="company_db")
cursor = db.cursor()

while True:
    print("\n--- Attendance System ---")
    print("1. Add | 2. Show | 3. Delete | 4. Update | 5. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Name: ")
        salary = int(input("Salary: "))
        cursor.execute("INSERT INTO attendance (name, salary) VALUES (%s, %s)", (name, salary))
        db.commit()

    elif choice == '2':
        cursor.execute("SELECT * FROM attendance")
        for row in cursor.fetchall():
            print(row)

    elif choice == '3':
        name = input("Delete Name: ")
        cursor.execute("DELETE FROM attendance WHERE name = %s", (name,))
        db.commit()

    elif choice == '4':
        name = input("Name to update: ")
        salary = int(input("New Salary: "))
        cursor.execute("UPDATE attendance SET salary = %s WHERE name = %s", (salary, name))
        db.commit()

    elif choice == '5':
        print("Exiting...")
        break