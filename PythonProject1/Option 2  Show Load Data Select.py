import mysql.connector

# 1. Connection (Database kooda link)
db = mysql.connector.connect(host="localhost", user="root", password="Irshad1990*", database="company_db")
cursor = db.cursor()


# Database-la irundhu data-vai eduthu varum logic
cursor.execute("SELECT * FROM attendance")

# Ellaa row-aiyum eduthu 'results' nu oru petti-la podu
results = cursor.fetchall()

# Loop vachi ovvoru row-a print pannu
print("\n--- Attendance List ---")
for row in results:
    print(f"Name: {row[0]} | Salary: {row[1]}")