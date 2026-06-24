employees = []
pass_count = 0
fail_count = 0

for i in range(3):
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    employees.append(name)

    if marks >= 50:
        print(name, "PASS")
        pass_count = pass_count + 1
    else:
        print(name, "FAIL")
        fail_count = fail_count + 1

print("Total Employees:", len(employees))
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)