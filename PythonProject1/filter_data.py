import sqlite3

conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# WHERE command: "Product 'Mouse' ah irundha mattum kodu"
cursor.execute("SELECT * FROM Sales WHERE price > 100")

results = cursor.fetchall()
print("Price 100 mela:", results)

conn.close()

import sqlite3
conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM Sales WHERE price < 100")
results = cursor.fetchall()
print("Price 100 Keela:", results)


