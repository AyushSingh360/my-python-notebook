# Solutions – Object-Oriented Programming (OOP)
import abc

# Helper to print section headers
def print_header(title):
    print(f"\n=== {title} ===")

# =============================================================================
# EASY LEVEL
# =============================================================================

# 1. Basic Class
print_header("Exercise 1: Basic Class")
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def description(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

b = Book("The Hobbit", "J.R.R. Tolkien", 310)
print(b.description())

# 2. Instance Variables
print_header("Exercise 2: Instance Variables")
class Counter:
    def __init__(self):
        self.count = 0 
    
    def increment(self):
        self.count += 1

c = Counter()
c.increment()
c.increment()
print(f"Count: {c.count}")

# 3. Class Attributes
print_header("Exercise 3: Class Attributes")
class Employee:
    company_name = "TechCorp" # Shared by all instances

    def __init__(self, name):
        self.name = name

e1 = Employee("Alice")
e2 = Employee("Bob")
print(f"{e1.name} works at {e1.company_name}")
print(f"{e2.name} works at {e2.company_name}")

# 4. Simple Inheritance
print_header("Exercise 4: Simple Inheritance")
class Vehicle:
    def drive(self):
        return "Vroom!"

class Car(Vehicle):
    pass # Inherits everything

my_car = Car()
print(my_car.drive())

# 5. Method Overriding
print_header("Exercise 5: Method Overriding")
class Animal:
    def speak(self): return "..."

class Dog(Animal):
    def speak(self): return "Woof"

class Cat(Animal):
    def speak(self): return "Meow"

print(f"Dog: {Dog().speak()}")
print(f"Cat: {Cat().speak()}")

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

# 6. Encapsulation
print_header("Exercise 6: Encapsulation")
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(f"Balance: {acc.get_balance()}")
# print(acc.__balance) # Raises AttributeError

# 7. Constructors
print_header("Exercise 7: Constructors")
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(f"Area of 5x10 rectangle: {rect.area()}")

# 8. The __str__ Method
print_header("Exercise 8: Magic String Method")
class BookStr(Book):
    def __str__(self):
        return f"'{self.title}' by {self.author}"

b2 = BookStr("1984", "George Orwell", 328)
print(b2) # Uses __str__

# 9. Class Methods
print_header("Exercise 9: Static Method")
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(f"5 + 7 = {Calculator.add(5, 7)}")

# 10. Property Decorators
print_header("Exercise 10: Properties")
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius # Initialize internal attribute

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            # Absolute zero check
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

temp = Temperature(25)
temp.celsius = 100
print(f"Temp is {temp.celsius}C")
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Caught expected error: {e}")

# 11. Inheritance with Super
print_header("Exercise 11: Super()")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        # Call parent constructor to handle name and age
        super().__init__(name, age)
        self.student_id = student_id

s = Student("John", 20, "S12345")
print(f"Student: {s.name}, ID: {s.student_id}")

# =============================================================================
# HARD LEVEL
# =============================================================================

# 12. Multiple Inheritance
print_header("Exercise 12: Multiple Inheritance")
class Flyable:
    def fly(self): return "Flying high!"

class Swimmable:
    def swim(self): return "Swimming..."

class Duck(Flyable, Swimmable):
    pass

d = Duck()
print(d.fly())
print(d.swim())

# 13. Abstract Base Classes
print_header("Exercise 13: Abstract Base Classes")
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

c = Circle(5)
sq = Square(4)
print(f"Circle Area: {c.area()}")
print(f"Square Area: {sq.area()}")

# 14. Operator Overloading
print_header("Exercise 14: Operator Overloading")
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 4)
v2 = Vector(1, 1)
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")

# 15. Polymorphism
print_header("Exercise 15: Polymorphism")
def animal_sound(animal):
    print(animal.speak())

# Reusing classes from Ex 5
animal_sound(Dog())
animal_sound(Cat())

# 16. Custom Exceptions
print_header("Exercise 16: Custom Exceptions")
class InsufficientFundsError(Exception):
    pass

class Wallet:
    def __init__(self, balance):
        self.balance = balance
    
    def spend(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Cannot spend {amount}, have only {self.balance}")
        self.balance -= amount
        print(f"Spent {amount}. Remaining: {self.balance}")

w = Wallet(50)
try:
    w.spend(100)
except InsufficientFundsError as e:
    print(f"Error caught: {e}")

# 17. The Diamond Problem
print_header("Exercise 17: Diamond Problem")
class A:
    def show(self): print("A")
class B(A):
    def show(self): print("B")
class C(A):
    def show(self): print("C")
class D(B, C):
    pass

d_obj = D()
d_obj.show() # Prints B because B is first in MRO
print(f"MRO: {D.mro()}")

# 18. Slots
print_header("Exercise 18: Slots")
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
try:
    p.z = 3
except AttributeError as e:
    print(f"Caught expected error: {e}")

# =============================================================================
# BONUS CHALLENGES
# =============================================================================

# 19. Composition
print_header("Exercise 19: Composition")
class Engine:
    def start(self): return "Engine started"

class CarWithEngine:
    def __init__(self):
        self.engine = Engine() # Has-a relationship
    
    def start(self):
        return self.engine.start() # Delegation

my_car = CarWithEngine()
print(my_car.start())

# 20. Singleton
print_header("Exercise 20: Singleton")
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            # print("Creating new instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same object? {db1 is db2}")

# 21. Context Managers
print_header("Exercise 21: Context Managers")
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage
with FileManager('test.txt') as f:
    f.write("Hello form Context Manager!")

import os
print(f"File created: {os.path.exists('test.txt')}")
os.remove('test.txt') # Cleanup
