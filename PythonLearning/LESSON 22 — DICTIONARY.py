employee = {
    "name": "Irshad",
    "id": 101,
    "department": "Admin",
    "salary": 3000
}
print(employee)

employee = {
    "name": "Irshad",
    "id": 101,
    "salary": 3000
}

print(employee["name"])
print(employee["id"])
print(employee["salary"])

employee = {
    "name": "Irshad",
    "department": "Admin",
    "shift": "B",
    "salary": 3000
}
print(employee["name"])
print(employee["department"])
print(employee["shift"])
print(employee["salary"])

employee = {
    "name": "Irshad",
    "city": "Jeddah"
}

employee["city"] = "Tabuk"

print(employee["city"])


employee = {
    "name": "Irshad",
    "city": "Tabuk"
}

employee["salary"] = 3000
print(employee["salary"])

employee = {
    "name": "Irshad",
    "city": "Riyadh",
    "salary": 3000
}

for key in employee:
    print(key)


employee = {
    "name": "Irshad",
    "city": "Riyadh",
    "salary": 3000
}

for key in employee:
    print(key, employee[key])

employee = {
    "name": "Irshad",
    "city": "Riyadh",
    "salary": 3000
}

print(len(employee))

employee = {
    "name": "Irshad",
    "city": "Riyadh"
}

if "salary" in employee:
    print("FOUND")
else:
    print("NOT FOUND")

employee = {
    "name": "Irshad",
    "city": "Riyadh"
}

print(employee.get("salary", "Not Found"))  