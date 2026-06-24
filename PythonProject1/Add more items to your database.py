import sqlite3

conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# 1. Palaya table irundha delete pannitu pudhusa create pannuvom
cursor.execute("DROP TABLE IF EXISTS Sales")
cursor.execute("CREATE TABLE Sales (Product TEXT, Price INTEGER)")

# 2. Neraya data-vai insert panrom
items = [('Laptop', 1500), ('Mouse', 50), ('Keyboard', 100), ('Monitor', 500), ('Mouse', 30)]

# 'executemany' = Neraya data-vai ore thadavai insert panna (Professional method)
cursor.executemany("INSERT INTO Sales VALUES (?, ?)", items)

conn.commit()

# 3. Ippo check pannuvom
cursor.execute("SELECT * FROM Sales")
print(cursor.fetchall())

conn.close()