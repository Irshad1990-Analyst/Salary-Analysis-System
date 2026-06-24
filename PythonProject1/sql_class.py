import sqlite3

# 1. Connection: Database-ai connect panrom (Ithu illana pudhusa create pannum)
conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# 2. Table create panrom (SQL command)
cursor.execute('''CREATE TABLE IF NOT EXISTS Sales 
                  (Product TEXT, Price INTEGER)''')

# 3. Data-vai insert panrom
cursor.execute("INSERT INTO Sales VALUES ('Laptop', 1500)")
conn.commit()

# 4. Data-vai eduthu varrom (SQL SELECT command)
cursor.execute("SELECT * FROM Sales")
print(cursor.fetchall())

# 5. Connection-ai close panrom
conn.close()