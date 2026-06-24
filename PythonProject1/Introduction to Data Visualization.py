import matplotlib.pyplot as plt
import numpy as np

# Namma kitta irukkura data
names = ['Irshad', 'Shiva', 'Ahmed', 'Ayesha', 'Manager']
salary = [3000, 4000, 5000, 6000, 9000]

# Bar Chart create panrom
plt.bar(names, salary, color='skyblue')

# Labels & Title
plt.xlabel('Employees')
plt.ylabel('Salary')
plt.title('Company Salary Distribution')

# Chart-ai show panna
plt.show()