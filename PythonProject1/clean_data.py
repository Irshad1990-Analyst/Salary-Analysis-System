import pandas as pd
import numpy as np

# Sila data illaama irukkura 'Dirty' list
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Sales': [1500, np.nan, 100, np.nan] # NaN nu irukkuradhu dhaan "Missing Data"
}

df = pd.DataFrame(data)
print("Dirty Data:")
print(df)

import pandas as pd
import numpy as np

data = {'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'Sales': [1500, np.nan, 100, np.nan]}

df = pd.DataFrame(data)
df_clean = df.fillna(0)

print(df_clean)