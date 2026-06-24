def check_employee(name, salary):
    if salary >= 3000:
        return name, "PASS"
    else:
        return name, "FAIL"


employees = {
    "A": 2000,
    "B": 3000,
    "C": 4000
}

for name in employees:
    emp_name, status = check_employee(name, employees[name])
    print(emp_name, status)


def check(salary):
    if salary >= 3000:
        return "PASS"
    else:
        return "FAIL"


employees = {"A": 1000, "B": 3500}

for name in employees:
    print(name, check(employees[name]))