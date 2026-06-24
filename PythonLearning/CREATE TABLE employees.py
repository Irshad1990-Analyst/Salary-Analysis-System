## CREATE TABLE employees
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*",
    database="HR_DB"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT
)
""")

print("Table Created Successfully")
