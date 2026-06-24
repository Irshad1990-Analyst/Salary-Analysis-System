import pandas as pd

data = {'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse'],
        'Sales': [1500, 50, 1500, 100, 50]}

df = pd.DataFrame(data)
df_group = df.groupby('Product')['Sales'].sum()

print(df_group)
