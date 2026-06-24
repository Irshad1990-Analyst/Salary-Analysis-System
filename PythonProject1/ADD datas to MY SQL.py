import mysql.connector

# 1. Connection (Database kooda link)
db = mysql.connector.connect(host="localhost", user="root", password="Irshad1990*", database="company_db")
cursor = db.cursor()

# 2. Input vangum logic
print("--- Attendance System ---")
name = input("Enter Name: ")
salary = int(input("Enter Salary: "))

# 3. Database-kulla anuppum logic
sql = "INSERT INTO attendance (name, salary) VALUES (%s, %s)"
val = (name, salary)

cursor.execute(sql, val)
db.commit()

print("Data added successfully!")