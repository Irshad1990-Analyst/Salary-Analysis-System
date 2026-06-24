# 1. Base Class with Encapsulation (Data Protection)
class MarineAsset:
    def __init__(self, name, asset_id):
        self.name = name
        self.__asset_id = asset_id  # Private data (Encapsulation)

    def get_id(self):
        return self.__asset_id

# 2. Inheritance & Polymorphism
class CargoVessel(MarineAsset):
    def status_report(self):
        return f"{self.name} (ID: {self.get_id()}) is carrying containers."

class TankerVessel(MarineAsset):
    def status_report(self):
        return f"{self.name} (ID: {self.get_id()}) is transporting oil."

# 3. Execution
fleet = [CargoVessel("Neom-C1", "N-001"), TankerVessel("Neom-T1", "N-002")]

for vessel in fleet:
    print(vessel.status_report()) # Polymorphism: Same method, different outcome!


class Staff: # Blueprint 1
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # __ (Double underscore) = Lock panni vechuruken.

    def get_salary(self):
        return self.__salary # Function moolama mattum dhan salary-ai paarka mudiyum.

class Attendance(Staff): # Blueprint 2 (Staff-kitta irundhu ellathaiyum vangukirathu)
    def mark_attendance(self):
        print(f"{self.name} is present.")

# Execution
e1 = Attendance("Irshad", 5000)
e1.mark_attendance()
print(f"Salary: {e1.get_salary()}")

# 1. Base Class: Ellarukkum common-ana vishayam
class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Encapsulation: Lock panna petti (Private)

    def show_salary(self):
        return self.__salary  # Lock-ai thirakka oru vazhi

# 2. Inheriting & Polymorphism: 'Manager' and 'Engineer'
class Manager(Staff): # Inheritance: Staff-kitta irundhu powers-ai vanguthu
    def get_role(self):
        return "Role: Manager" # Polymorphism: Ivanga oru vesham

class Engineer(Staff): # Inheritance: Staff-kitta irundhu powers-ai vanguthu
    def get_role(self):
        return "Role: Engineer" # Polymorphism: Ivanga innonru vesham

# 3. Execution
team = [Manager("Irshad", 8000), Engineer("Kumar", 5000)]

for person in team:
    print(f"{person.name} | {person.get_role()} | Salary: {person.show_salary()}")