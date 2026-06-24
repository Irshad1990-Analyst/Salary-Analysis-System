import sqlite3

conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# GROUP BY command: Product-ai vachi group panni, Price-ai total sei
cursor.execute("SELECT Product, SUM(Price) FROM Sales GROUP BY Product")

results = cursor.fetchall()
print("Product-wise Total Sales:", results)

conn.close()