import mysql.connector

# 1. Connection (Database kooda link)
db = mysql.connector.connect(host="localhost", user="root", password="Irshad1990*", database="company_db")
cursor = db.cursor()

# Delete logic
name_to_delete = "Irshad" # Yaarai delete panna porom?

# 'DELETE FROM table WHERE column = value'
sql = "DELETE FROM attendance WHERE name = %s"
val = (name_to_delete,) # Oru value mattum iruntha comma (,) podanum

cursor.execute(sql, val)
db.commit()

print(f"{cursor.rowcount} record deleted!")