for employee in range(5):
    print("Check attendance")

for i in range(1,6):
    print("i")


for i in range(3):
    print(i)

for i in range(1, 6):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")


for i in range(1, 6):
    attendance = i * 20

    if attendance >= 80:
        print("Employee", i, "Pass")
    else:
        print("Employee", i, "Fail")

for i in range(1, 6):
    salary = i * 1000

    if salary >= 3000:
        print("Employee", i, "High Salary")
    else:
        print("Employee", i, "Low Salary")


for i in range(1, 4):
    if i == 2:
        print("Two")
    else:
        print(i)

for i in range(1, 6):
    attendance = int(input(f"Enter Attendance for Employee {i}: "))

    if attendance >= 80:
        print("Employee", i, "PASS")
    else:
        print("Employee", i, "FAIL")