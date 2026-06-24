class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"


c = Cat()
d = Dog()

print(c.sound())
print(d.sound())

class Bird:
    def move(self):
        return "Fly"

class Fish:
    def move(self):
        return "Swim"

b = Bird()
f = Fish()

print(b.move())
print(f.move())

class Car:
    def start(self):
        return "Car Started"

class Computer:
    def start(self):
        return "Computer Started"

c = Car()
p = Computer()

print(c.start())
print(p.start())