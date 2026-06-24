
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*",
    database="HR_DB"
)

cursor = conn.cursor()

sql = "INSERT INTO employees (id, name, salary) VALUES (%s, %s, %s)"
val = (1, "Irshad", 5000)

cursor.execute(sql, val)

conn.commit()

print("Employee Inserted Successfully")
