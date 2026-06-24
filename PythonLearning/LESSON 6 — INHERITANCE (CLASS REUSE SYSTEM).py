class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        return self.name, self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus


m1 = Manager("Irshad", 3000, 1000)

print(m1.show())
print(m1.total_salary())

class A:
    def show(self):
        return "Hello"

class B(A):
    pass

obj = B()
print(obj.show())

class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

obj = B()
print(obj.show())

class A:
    def show(self):
        return "Parent"

class B(A):
    pass

obj = B()
print(obj.show())