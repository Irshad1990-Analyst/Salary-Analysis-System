import numpy as np

# Employee Salary Data
salary_data = np.array([3000, 4000, 5000, 6000, 7000, 8000])

# Stats Calculation
total = np.sum(salary_data)      # Motham
average = np.mean(salary_data)   # Average
minimum = np.min(salary_data)    # Lowest salary
maximum = np.max(salary_data)    # Highest salary
median = np.median(salary_data) # Naduvula irikira data

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Min: {minimum}")
print(f"Max: {maximum}")
print(f"Median: {median}")