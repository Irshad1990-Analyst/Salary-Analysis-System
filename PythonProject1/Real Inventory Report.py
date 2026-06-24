import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Dummy data (Sila data illama 'Dirty'-a irukkum)
data = {'Product': ['Laptop', 'Mouse', 'Laptop', 'Keyboard', 'Mouse', 'Monitor', 'Keyboard'],
        'Sales': [1500, np.nan, 1500, 100, 50, 500, np.nan]}
df = pd.DataFrame(data)
df.to_excel('final_sales.xlsx', index=False)

# 2. Data Load & Clean
df_load = pd.read_excel('final_sales.xlsx')
df_clean = df_load.fillna(0)

# 3. Analysis (Grouping)
final_report = df_clean.groupby('Product')['Sales'].sum()

# 4. Visualization
final_report.plot(kind='bar', color='green')
plt.title('Final Sales Report')
plt.show()

print("Report Ready! Analysis complete.")