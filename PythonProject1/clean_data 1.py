import sqlite3

conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# WHERE Price IS NOT NULL: Price empty-a illatha row-ai mattum kodu
cursor.execute("SELECT * FROM Sales_Report WHERE Sales IS NOT NULL")

results = cursor.fetchall()
print("Cleaned Data (No None values):", results)

conn.close()