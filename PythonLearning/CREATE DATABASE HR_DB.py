## CREATE DATABASE HR_DB;
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS HR_DB")

print("Database Created Successfully")