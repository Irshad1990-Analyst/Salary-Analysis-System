import pandas as pd
import matplotlib.pyplot as plt

data = {'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'Sales': [1500, 50, 100, 500]}

df = pd.DataFrame(data)

# Chart-ai uruvaakkum magic
df.plot(kind='bar', x='Product', y='Sales')
plt.show()