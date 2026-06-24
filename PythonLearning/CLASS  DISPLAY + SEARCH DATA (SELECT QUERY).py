## SEARCH DATA
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*",
    database="HR_DB"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")

results = cursor.fetchall()

for row in results:
    print(row)

name = input("Enter name to search: ")

sql = "SELECT * FROM employees WHERE name = %s"
val = (name,)

cursor.execute(sql, val)

result = cursor.fetchall()

for row in result:
    print(row)