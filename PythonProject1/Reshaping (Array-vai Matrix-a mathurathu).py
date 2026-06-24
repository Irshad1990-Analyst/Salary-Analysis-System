import numpy as np

# Namma kitta 6 salary data irukkunnu vechukonga
salary_data = np.array([3000, 4000, 5000, 6000, 7000, 8000])

# Ippo idhai 2 row, 3 column ulla table-a (Matrix) mathalam
matrix = salary_data.reshape(2, 3)

print("Original Array:")
print(salary_data)
print("\nReshaped Matrix (2x3):")
print(matrix)