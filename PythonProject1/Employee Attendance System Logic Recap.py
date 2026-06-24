# 1. Dictionary (L22) - Oru employee-oda file
emp1 = {"Name": "Irshad", "Status": "Present"}
emp2 = {"Name": "Elmer", "Status": "Absent"}
emp3 = {"Name": "John", "Status": "Present"}

# 2. List (L23-24) - Ellaa employee-um irukkura oru koodai
attendance_list = [emp1, emp2, emp3]

# 3. Loop & Logic (L25-26) - Koodaikkulla irukkuravangala pathi theriya patharathum, filter panrathum
print("Today's Attendance Report:")

for employee in attendance_list: # Loop: Ovvoru alaiya eduthu kodukkum
    # If Condition: Absent aanavangala mattum kandupidikkum
    if employee["Status"] == "Absent":
        print(f"Alert! {employee['Name']} is absent today.")
    else:
        print(f"{employee['Name']} is present.")