import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

# 1. Database Connection
db = mysql.connector.connect(host="localhost", user="root", password="Irshad1990*", database="company_db")
cursor = db.cursor()
cursor.execute("SELECT name, salary FROM attendance") # Name-um salary-um edukrom
data = cursor.fetchall()

# 2. Data Cleaning
names = [row[0] for row in data]
salary = [row[1] for row in data]

# 3. Visualization
plt.figure(figsize=(8, 6)) # Chart-oda size-ai define panrom
plt.bar(names, salary, color='green')
plt.title("Final Salary Report")
plt.xlabel("Employees")
plt.ylabel("Salary")

# 4. Save the Chart as a file
plt.savefig("salary_report.png")
print("Report saved as 'salary_report.png' successfully!")