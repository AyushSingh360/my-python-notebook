# Comprehensive Examples of Object-Oriented Programming (OOP) in Python

# ==========================================
# 1. Basic Class and Instance
# ==========================================
class Dog:
    """A simple class representing a dog."""
    
    # Class Attribute (Shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Constructor: Initializes the object."""
        # Instance Attributes (Unique to each instance)
        self.name = name
        self.age = age
        
    def description(self):
        """Instance Method"""
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        """Instance Method with arguments"""
        return f"{self.name} says {sound}."

print("=== 1. Basic Class & Instance ===")
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.description())  # Buddy is 9 years old.
print(miles.speak("Woof"))  # Miles says Woof.
print(f"Species: {buddy.species}") # Canis familiaris


# ==========================================
# 2. Encapsulation (Public, Protected, Private)
# ==========================================
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public
        self._type = "Checking"  # Protected (Convention: internal use)
        self.__balance = balance # Private (Name mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")

    def get_balance(self):
        return self.__balance

print("\n=== 2. Encapsulation ===")
account = BankAccount("Alice", 1000)
account.deposit(500)
print(f"Owner: {account.owner}")
print(f"Balance: ${account.get_balance()}")
# print(account.__balance) # AttributeError
# Accessing private member (Not recommended, but possible via name mangling)
print(f"Secret Access: {account._BankAccount__balance}")


# ==========================================
# 3. Inheritance & Super()
# ==========================================
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass # Abstract-ish

class Cat(Animal):
    def speak(self):
        return "Meow"

class Lion(Cat):
    def __init__(self, name, pride_size):
        super().__init__(name) # Call parent's __init__
        self.pride_size = pride_size
        
    def speak(self):
        # Extend parent's behavior
        parent_sound = super().speak() 
        return f"{parent_sound}... ROAR!"

print("\n=== 3. Inheritance & Super() ===")
simba = Lion("Simba", 10)
print(f"{simba.name} says: {simba.speak()}")


# ==========================================
# 4. Polymorphism
# ==========================================
class Shape:
    def area(self): pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self): return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self): return 3.14 * self.r ** 2

def print_area(shape_obj):
    # Polymorphism: function works with any object having an .area() method
    print(f"Area: {shape_obj.area()}")

print("\n=== 4. Polymorphism ===")
shapes = [Rectangle(10, 5), Circle(7)]
for shape in shapes:
    print_area(shape)


# ==========================================
# 5. Magic Methods (Dunder Methods)
# ==========================================
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        """User-friendly string representation (for print)"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer-friendly string representation (for shell/debugging)"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Overloads the + operator"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """Overloads the == operator"""
        return self.x == other.x and self.y == other.y

print("\n=== 5. Magic Methods ===")
v1 = Vector(2, 4)
v2 = Vector(5, -1)
print(f"v1: {v1}")          # Uses __str__
print(f"v1 + v2: {v1 + v2}") # Uses __add__
print(f"v1 == v2: {v1 == v2}") # Uses __eq__


# ==========================================
# 6. @property Decorator (Getters/Setters)
# ==========================================
class Product:
    def __init__(self, price):
        self._price = price # Note the underscore
        
    @property
    def price(self):
        """Getter"""
        return self._price
    
    @price.setter
    def price(self, value):
        """Setter with validation"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

print("\n=== 6. @property Decorator ===")
p = Product(50)
print(f"Price: {p.price}")
p.price = 75 # Calls setter
try:
    p.price = -10 # Raises Error
except ValueError as e:
    print(f"Error: {e}")


# ==========================================
# 7. Class vs Static Methods
# ==========================================
import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_birth_year(cls, name, year):
        """Class method: Alternative constructor"""
        current_year = datetime.date.today().year
        return cls(name, current_year - year)
    
    @staticmethod
    def is_adult(age):
        """Static method: Utility function, doesn't need self or cls"""
        return age >= 18

print("\n=== 7. Class & Static Methods ===")
p1 = Person("Alice", 25)
p2 = Person.from_birth_year("Bob", 2000)
print(f"{p2.name} is {p2.age} years old.")
print(f"Is {p2.name} an adult? {Person.is_adult(p2.age)}")


# ==========================================
# 8. __slots__ for Memory Optimization
# ==========================================
class PointWithSlots:
    """Restricts attributes to ONLY x and y. Saves memory."""
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== 8. Slots ===")
pt = PointWithSlots(10, 20)
# pt.z = 30 # AttributeError: 'PointWithSlots' object has no attribute 'z'
print("Slots successfully prevented dynamic attribute creation.")


# ==========================================
# 9. Abstract Base Classes (ABCs)
# ==========================================
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal")

# p = PaymentProcessor() # TypeError: Can't instantiate abstract class
print("\n=== 9. Abstract Base Classes ===")
processor = PayPal()
processor.process_payment(100)
