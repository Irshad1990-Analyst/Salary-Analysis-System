import pandas as pd

# 1. Namma kitta irukkura data
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [1500, 50, 100, 500]
}

# 2. DataFrame-ai create pannuvom
df = pd.DataFrame(data)

# 3. Table-ai print pannuvom
print("Namoda Smart Table:")
print(df)

# 4. Innum oru "Smart" velai: Price-oda Mean (Average) kandu pidippom
average_price = df['Price'].mean()
print("\nEllathoda Average Price:", average_price)