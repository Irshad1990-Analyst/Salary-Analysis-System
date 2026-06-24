class Ship:
    def safety_check(self):
        print("General safety check done.")

class Tanker(Ship):
    def safety_check(self):
        print("Tanker: Checking oil pressure and leaks.") # Tanker-oda vesham

class CargoShip(Ship):
    def safety_check(self):
        print("Cargo: Checking container locks and weight.") # Cargo-oda vesham

# Execution
my_ships = [Tanker(), CargoShip()]

for ship in my_ships:
    ship.safety_check() # Same name, different actions!