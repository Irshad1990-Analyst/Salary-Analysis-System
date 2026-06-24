import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*"
)

print("MySQL Connected Successfully")

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Irshad1990*"
)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)



