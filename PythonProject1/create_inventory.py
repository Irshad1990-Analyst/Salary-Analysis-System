import sqlite3

conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# 1. Inventory table-ai create panrom
cursor.execute("""
CREATE TABLE IF NOT EXISTS Inventory (
    Product TEXT,
    Quantity INTEGER
)
""")

# 2. Sila dummy data-vai add panrom
data = [('Laptop', 10), ('Mouse', 50), ('Keyboard', 20), ('Monitor', 15)]
cursor.executemany("INSERT INTO Inventory VALUES (?, ?)", data)

conn.commit()
print("Inventory table ready aayiduchu!")
conn.close()