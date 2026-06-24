import sqlite3
import pandas as pd

conn = sqlite3.connect('my_shop.db')
df = pd.read_sql_query("SELECT * FROM Sales_Report", conn)

# 1. CLEANING: NaN irukkura row-ai delete panna:
df_cleaned = df.dropna()

# 2. ALTERNATIVE: NaN irukkura edathula 0 pottu nirappa:
# df_filled = df.fillna(0)

print("Cleaned Data (NaN rows deleted):")
print(df_cleaned)

conn.close()