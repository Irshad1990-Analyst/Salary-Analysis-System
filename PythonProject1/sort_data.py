import sqlite3

conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# 1. Price-ai vachi 'Ascending' (Small to Big) order
cursor.execute("SELECT * FROM Sales ORDER BY Price ASC")
print("Price Small to Big:", cursor.fetchall())

# 2. Price-ai vachi 'Descending' (Big to Small) order
cursor.execute("SELECT * FROM Sales ORDER BY Price DESC")
print("Price Big to Small:", cursor.fetchall())

conn.close()