import mysql.connector

# 1. Connection (Database kooda link)
db = mysql.connector.connect(host="localhost", user="root", password="Irshad1990*", database="company_db")
cursor = db.cursor()

# Update logic
new_salary = 9000
name_to_update = "Mohamed"

# 'UPDATE table SET column = new_value WHERE column = value'
sql = "UPDATE attendance SET salary = %s WHERE name = %s"
val = (new_salary, name_to_update)

cursor.execute(sql, val)
db.commit()

print(f"{cursor.rowcount} record updated!")