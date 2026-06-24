import sqlite3

conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# INNER JOIN: Rendu table-layum irukkura common items-ai mattum join pannu
query = """
SELECT Sales_Report.Product, Sales_Report.Sales, Inventory.Quantity
FROM Sales_Report
INNER JOIN Inventory ON Sales_Report.Product = Inventory.Product
"""

cursor.execute(query)
results = cursor.fetchall()

print("Joined Data Report:", results)

conn.close()