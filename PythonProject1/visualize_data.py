import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('my_shop.db')
cursor = conn.cursor()

# SQL query vachi data-vai eduppom
cursor.execute("SELECT Product, Sales FROM Sales_Report WHERE Sales IS NOT NULL")
data = cursor.fetchall()

# Data-vai chart-kku etharppol pirippom
products = [row[0] for row in data]
sales = [row[1] for row in data]

# Chart create panrom
plt.bar(products, sales, color='skyblue')
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Product-wise Sales Report')
plt.show()

conn.close()