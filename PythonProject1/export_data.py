import sqlite3
import pandas as pd

conn = sqlite3.connect('my_shop.db')
df = pd.read_sql_query("SELECT * FROM Sales_Report", conn)
df_cleaned = df.dropna()

# Grouping
grouped_df = df_cleaned.groupby('Product')['Sales'].sum().reset_index()

# 1. Excel-la save panrom (Report.xlsx)
grouped_df.to_excel('Final_Sales_Report.xlsx', index=False)

print("Report Excel-la save aayiduchu! Unga project folder-ai paarunga.")

conn.close()