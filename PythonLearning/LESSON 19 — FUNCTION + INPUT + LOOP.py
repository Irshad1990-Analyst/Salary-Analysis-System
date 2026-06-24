def check_result(name, marks):
    if marks >= 50:
        print(name, "PASS")
    else:
        print(name, "FAIL")


for i in range(3):
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    check_result(name, marks)


def show(name, marks):
    if marks >= 60:
        print(name, "PASS")
    else:
        print(name, "FAIL")

for i in range(2):
    show("Irshad", 70)