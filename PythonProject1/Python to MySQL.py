import mysql.connector

# Adhu illaama connect pannu
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*"
)

cursor = db.cursor()
# Database-ai create pannu
cursor.execute("CREATE DATABASE IF NOT EXISTS company_db")
# Ippo connect pannu
cursor.execute("USE company_db")

import mysql.connector

# Connection Setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*",
    database="company_db"
)

cursor = db.cursor()
# Table-ai create pannu
cursor.execute("CREATE TABLE IF NOT EXISTS attendance (name VARCHAR(50), salary INT)")
cursor.execute("INSERT INTO attendance (name, salary) VALUES ('Irshad', 5000)")
db.commit()

print("Data saved to database!")

