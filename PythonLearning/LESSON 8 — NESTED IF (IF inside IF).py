age = 20
salary = 5000

if age >= 18:
    if salary >= 4000:
        print("Eligible for Loan")

attendance = 85
salary = 4500

if attendance >= 80:
    if salary >= 5000:
        print("High Priority Employee")
    else:
        print("Normal Employee")


age = int(input("Enter Age: "))
attendance = int(input("Enter Attendance: "))
salary = int(input("Enter Salary: "))

if age >= 18:
    if attendance >= 80:
        if salary >= 4000:
            print("APPROVED - High Level Employee")
        else:
            print("APPROVED - Low Salary Employee")
    else:
        print("NOT APPROVED - Low Attendance")
else:
    print("NOT APPROVED - Age Problem")