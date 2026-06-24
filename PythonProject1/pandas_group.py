import sqlite3
import pandas as pd

conn = sqlite3.connect('my_shop.db')
df = pd.read_sql_query("SELECT * FROM Sales_Report", conn)
df_cleaned = df.dropna()

# 1. Product-ai group panni, total sales-ai calculate panrom
grouped_df = df_cleaned.groupby('Product')['Sales'].sum().reset_index()

print("Grouped Total Sales:")
print(grouped_df)

conn.close()