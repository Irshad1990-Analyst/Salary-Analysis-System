import sqlite3
import pandas as pd # Pandas-ai import panrom

# 1. Database-kku connect panrom
conn = sqlite3.connect('my_shop.db')

# 2. SQL query-ai Pandas-oda 'read_sql_query' function vachi read panrom
df = pd.read_sql_query("SELECT * FROM Sales_Report", conn)

# 3. Ippo idhai oru DataFrame-a print panrom
print("Pandas DataFrame:")
print(df)

conn.close()