import mysql.connector
import numpy as np

# 1. Database-la irundhu data-vai edukka
db = mysql.connector.connect(host="localhost", user="root", password="Irshad1990*", database="company_db")
cursor = db.cursor()
cursor.execute("SELECT salary FROM attendance")
data = cursor.fetchall()

# 2. Data-vai clean panni NumPy array-a matha
# fetchall() oru tuple-a kudukkum, athai list-a mathanum
salary_list = [row[0] for row in data]
salary_array = np.array(salary_list)

# 3. Statistical Analysis
print("--- Company Salary Report ---")
print(f"Total Employees: {len(salary_array)}")
print(f"Total Budget: {np.sum(salary_array)}")
print(f"Average Salary: {np.mean(salary_array)}")
print(f"Highest Salary: {np.max(salary_array)}")