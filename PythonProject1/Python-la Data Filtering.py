import pandas as pd

# Ithu unga previous grouped_df nu vechukurom
data = {'Product': ['Keyboard', 'Laptop', 'Monitor', 'Mouse'],
        'Sales': [100.0, 3000.0, 500.0, 50.0]}
grouped_df = pd.DataFrame(data)

# 1. FILTERING: 500-kku mela Sales irukkurathai matum edukka
high_sales = grouped_df[grouped_df['Sales'] >= 500]

print("High Sales Products (>= 500):")
print(high_sales)
