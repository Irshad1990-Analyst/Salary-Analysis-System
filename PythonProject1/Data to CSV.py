import pandas as pd # Pandas-a 'pd' nu kooduvom

# 1. Un data-vai list-a create pannu
data = {
    "Name": ["Irshad", "Kumar", "Siva"],
    "Role": ["Coordinator", "Manager", "Engineer"],
    "Salary": [8000, 10000, 7000]
}

# 2. Intha data-vai 'DataFrame' (Excel table) maathu
df = pd.DataFrame(data)

# 3. Excel/CSV-la save pannu
df.to_csv("Neom_Report.csv", index=False)

print("Report created successfully!")