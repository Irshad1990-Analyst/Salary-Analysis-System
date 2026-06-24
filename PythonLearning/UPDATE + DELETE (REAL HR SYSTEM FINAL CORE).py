## UPDATE (SALARY CHANGE)
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*",
    database="HR_DB"
)

cursor = conn.cursor()

emp_id = int(input("Enter ID to update salary: "))
new_salary = int(input("Enter new salary: "))

sql = "UPDATE employees SET salary = %s WHERE id = %s"
val = (new_salary, emp_id)

cursor.execute(sql, val)

conn.commit()

print("Salary Updated Successfully")

##PART 2: DELETE EMPLOYEE
emp_id = int(input("Enter ID to delete: "))

sql = "DELETE FROM employees WHERE id = %s"
val = (emp_id,)

cursor.execute(sql, val)

conn.commit()

print("Employee Deleted Successfully")