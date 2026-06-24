class Employee:                 # 1. 'class' na oru blueprint (Design). 'Employee' nu peru vachirukkom.
    def __init__(self, name):   # 2. 'def' na oru velai (Function). '__init__' na, pusaala vandhu munnadiye set panra 'Setup' velai.
        self.name = name        # 3. 'self.name' na, intha card-kulla 'name'-ai store panni vechukkoda nu artham.

    def display(self):          # 4. Innonru 'def' velai. 'display' na veliya kaatradhu.
        print(f"Name: {self.name}") # 5. 'print' na screen-la kattu.

class Manager(Employee):        # 6. 'Manager' nu pudhu blueprint. Bracket-kulla 'Employee' irukka?
                                #    Athu dhaan 'Inheritance' (Appa-kitta irundhu kidaikkurathu).
    def give_permission(self):  # 7. 'Manager'-kku nu sonthama oru velai.
        print(f"{self.name} is giving permission.") # 8. Manager-oda sontha velai.

m = Manager("Irshad")           # 9. 'm' nu oru manager-ai create panrom. Avar peru 'Irshad'.
m.display()                     # 10. Avar 'Employee' nu blueprint-la irundha velaiyai seiyararu.
m.give_permission()             # 11. Manager-oda sontha velaiyai seiyararu.


name = "Irshad"
department = "Marine"

# f illama potta:
print("Name: self.name")
# Output: Name: self.name (Ithu dhaan varum, computer-ku self.name-na enna nu theriyaathu)

# f-string vachi potta:
print(f"Name: {name}, Dept: {department}")
# Output: Name: Irshad, Dept: Marine (Ipo puriyudha?)

# 1. Base Class (Common for all ships)
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def status(self):
        print(f"Ship: {self.name}, Capacity: {self.capacity} Tons")


# 2. Child Class (Container Ship - Inherits everything from Ship)
class ContainerShip(Ship):
    def load_container(self):
        print(f"{self.name} is loading containers.")


# 3. Child Class (Tanker - Inherits everything from Ship)
class Tanker(Ship):
    def pump_oil(self):
        print(f"{self.name} is pumping oil.")


# Execution
my_ship = ContainerShip("Neom-Carrier-01", 5000)
my_ship.status()  # Common method (inherited)
my_ship.load_container()  # Own method
# 1. Base Class (Ellaa marine employee-kum idhu common)
class ShipEmployee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_profile(self):
        print(f"Name: {self.name} | ID: {self.emp_id}")

# 2. Child Class (Manager-kku special authority irukkum)
class ShipManager(ShipEmployee):
    def __init__(self, name, emp_id, department):
        # 'super()' na Appa class-oda setup-ai (init) koopidurathu
        super().__init__(name, emp_id)
        self.department = department

    def manage_operation(self):
        print(f"Manager {self.name} is coordinating marine operations in {self.department}.")

# 3. Execution (Namma Neom project-oda team)
# Manager-ai create panrom
mgr = ShipManager("Irshad", "NEOM-007", "Marine Coordination")

# Avaroda profile-ai paarkkalam (Idhu 'ShipEmployee' class-la irundhu vandhathu)
mgr.show_profile()

# Avaroda special velai (Idhu 'ShipManager' class-la irukkura sontha velai)
mgr.manage_operation()