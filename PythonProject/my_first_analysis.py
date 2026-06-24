import pandas as pd

# Python-kku data-vai kudukrom (Dataframe)
data = {
    'Product': ['Laptop', 'Headphones', 'Laptop', 'Keyboard', 'Mouse'],
    'Sales': [1500, 200, 1500, 100, 50]
}

# Idhai table-a mathi 'df' nu peru vaikrom
df = pd.DataFrame(data)

# Ippo andha table-ai print panni paapom
print(df)

# Laptop-oda total sales-ai kandu pidippom
total_laptop = df[df['Product'] == 'Laptop']['Sales'].sum()
print("\nLaptop Total Sales:", total_laptop)