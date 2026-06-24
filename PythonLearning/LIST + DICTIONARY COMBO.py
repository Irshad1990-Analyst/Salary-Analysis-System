employee = {
    "id": 1,
    "name": "Irshad",
    "salary": 5000
}
print(employee)
print(employee["name"])
employee["salary"] = 7000
print(employee)

employees = [
    {"id": 1, "name": "Irshad", "salary": 5000},
    {"id": 2, "name": "Ahmed", "salary": 6000}]
for e in employees:
    print(e["id"], e["name"], e["salary"])