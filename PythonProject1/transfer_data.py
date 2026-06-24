import pandas as pd
import sqlite3

# 1. Excel-ai read panrom
df = pd.read_excel('final_sales.xlsx')

# 2. Database connection create panrom
conn = sqlite3.connect('my_shop.db')

# 3. Pandas DataFrame-ai SQL table-a maathrom (Magic happens here!)
df.to_sql('Sales_Report', conn, if_exists='replace', index=False)

print("Excel data database-kku poiyachu!")

conn.close()

