import numpy as np

# 1. Normal List vs NumPy Array
salary_list = [2500, 3500, 4500] # Normal list
salary_array = np.array([2500, 3500, 4500]) # NumPy Array

# 2. Logic: Salary-oda oru 500 bonus-a serthu paarkalam
bonus_salary = salary_array + 500

print(bonus_salary)
print(bonus_salary[0])
print(bonus_salary[1:3])