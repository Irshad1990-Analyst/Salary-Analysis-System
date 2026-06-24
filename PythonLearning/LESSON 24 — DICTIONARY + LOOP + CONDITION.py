employees = {
    "Irshad": 3500,
    "Ahmed": 2500,
    "Salim": 4000
}

for name in employees:
    if employees[name] >= 3000:
        print(name, "HIGH SALARY")
    else:
        print(name, "LOW SALARY")


employees = {
    "A": 2000,
    "B": 3000,
    "C": 4000
}

for name in employees:
    if employees[name] >= 3000:
        print(name, "PASS")
    else:
        print(name, "FAIL")