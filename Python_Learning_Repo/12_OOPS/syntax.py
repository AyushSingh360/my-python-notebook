# Basic Class Syntax

class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name          # Instance attribute
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

# Inheritance
class Poodle(Dog):
    def dance(self):
        return "Dancing!"

# Usage
d = Dog("Buddy", 5)
print(d.bark())
p = Poodle("Fifi", 3)
print(p.bark())
print(p.dance())
