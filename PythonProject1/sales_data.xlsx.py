import pandas as pd

# 1. Dummy data create panrom
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Sales': [1500, 50, 100, 500]
}
df = pd.DataFrame(data)

# 2. Idhai Excel file-a mathi save panrom
df.to_excel('sales_data.xlsx', index=False)
print("Excel file create aaiduchu!")

# Excel file-ai read panrom
df_read = pd.read_excel('sales_data.xlsx')

# Data-vai paapom
print("\nExcel-la irundhu vandha data:")
print(df_read)

# Logic: Sales 100-kku mela irukkura items-ai mattum print pannu
high_sales = df_read[df_read['Sales'] > 100]
print("\nHigh Sales Items:")
print(high_sales)