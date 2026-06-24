class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public (Ellarukkum theriyum)
        self.__salary = salary    # Private (Idhu dhaan LOCK panna data)

    def show_salary(self):
        print(f"Salary is: {self.__salary}")

# Execution
emp = Employee("Irshad", 10000)

print(emp.name)       # Ithu work aagum (Irshad)
# print(emp.__salary) # Ithu ERROR kodukkum! (Yen na idhu LOCKED)
emp.show_salary()     # Ithu mattum dhaan velai seiyum