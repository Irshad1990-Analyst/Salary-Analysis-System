## CLASS: DYNAMIC INSERT SYSTEM
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*",
    database="HR_DB"
)

cursor = conn.cursor()

emp_id = int(input("Enter ID: "))
name = input("Enter Name: ")
salary = int(input("Enter Salary: "))

sql = "INSERT INTO employees (id, name, salary) VALUES (%s, %s, %s)"
val = (emp_id, name, salary)

cursor.execute(sql, val)

conn.commit()

print("Employee Added Successfully")