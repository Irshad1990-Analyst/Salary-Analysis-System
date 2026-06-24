def greet():
    print("Hello Students")

greet()
def greet(name):
    print("Hello", name)

greet("Irshad")
greet("Ahmed")

def check_result(name, marks):
    if marks >= 50:
        print(name, "PASS")
    else:
        print(name, "FAIL")

check_result("Irshad", 80)
check_result("Ahmed", 40)


def show(name):
    print("Welcome", name)

show("Irshad")
show("Ahmed")