# Solutions – Object-Oriented Programming

from abc import ABC, abstractmethod

# =============================================================================
# EASY LEVEL
# =============================================================================

# 1. Basic Class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

print("=== 1. Basic Class ===")
b = Book("1984", "George Orwell", 328)
print(b.description())

# 2. Instance Variables
class Counter:
    def __init__(self):
        self.count = 0 
    
    def increment(self):
        self.count += 1

print("\n=== 2. Instance Variables ===")
c = Counter()
c.increment()
print(c.count) # 1

# 3. Class Attributes
class Employee:
    company_name = "TechCorp" # Shared by all instances

    def __init__(self, name):
        self.name = name

print("\n=== 3. Class Attributes ===")
e1 = Employee("Alice")
e2 = Employee("Bob")
print(e1.company_name) # TechCorp
print(e2.company_name) # TechCorp

# 4. Simple Inheritance
class Vehicle:
    def drive(self):
        return "Vroom!"

class Car(Vehicle):
    pass

print("\n=== 4. Simple Inheritance ===")
my_car = Car()
print(my_car.drive())

# 5. Method Overriding
class Animal:
    def speak(self): return "..."

class Dog(Animal):
    def speak(self): return "Woof"

class Cat(Animal):
    def speak(self): return "Meow"

print("\n=== 5. Method Overriding ===")
print(Dog().speak())
print(Cat().speak())

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

# 6. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal")

    def get_balance(self):
        return self.__balance

print("\n=== 6. Encapsulation ===")
acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())
# print(acc.__balance) # AttributeError

# 7. Constructors
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

print("\n=== 7. Constructors ===")
rect = Rectangle(5, 10)
print(f"Area: {rect.area()}")

# 8. The __str__ Method
class BookRepr(Book):
    def __str__(self):
        return f"'{self.title}' by {self.author}"

print("\n=== 8. Magic String Method ===")
b2 = BookRepr("Dune", "Frank Herbert", 412)
print(b2)

# 9. Class Methods
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print("\n=== 9. Static Method ===")
print(Calculator.add(5, 7))

# 10. Property Decorators
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

print("\n=== 10. Properties ===")
t = Temperature(25)
t.celsius = 30
print(t.celsius)
try:
    t.celsius = -300
except ValueError as e:
    print(e)

# 11. Inheritance with Super
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # Call parent constuctor
        self.student_id = student_id

print("\n=== 11. Super() ===")
s = Student("John", 20, "S12345")
print(f"{s.name}, ID: {s.student_id}")

# =============================================================================
# HARD LEVEL
# =============================================================================

# 12. Multiple Inheritance
class Flyable:
    def fly(self): return "Flying high!"

class Swimmable:
    def swim(self): return "Swimming..."

class Duck(Flyable, Swimmable):
    pass

print("\n=== 12. Multiple Inheritance ===")
d = Duck()
print(d.fly())
print(d.swim())

# 13. Abstract Base Classes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius

print("\n=== 13. Abstract Base Classes ===")
# s = Shape() # TypeError: Can't instantiate abstract class
c = Circle(5)
print(f"Circle Area: {c.area()}")

# 14. Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print("\n=== 14. Operator Overloading ===")
v1 = Vector(2, 4)
v2 = Vector(1, 1)
v3 = v1 + v2
print(v3)

# 15. Polymorphism
def animal_sound(animal):
    print(animal.speak())

print("\n=== 15. Polymorphism ===")
animal_sound(Dog())
animal_sound(Cat())

# 16. Custom Exceptions
class InsufficientFundsError(Exception):
    pass

class Wallet:
    def __init__(self, amt):
        self.balance = amt
    
    def spend(self, amt):
        if amt > self.balance:
            raise InsufficientFundsError(f"Need {amt}, have {self.balance}")
        self.balance -= amt

print("\n=== 16. Custom Exceptions ===")
w = Wallet(50)
try:
    w.spend(100)
except InsufficientFundsError as e:
    print(f"Caught error: {e}")

# 17. The Diamond Problem
class A:
    def show(self): print("A")
class B(A):
    def show(self): print("B")
class C(A):
    def show(self): print("C")
class D(B, C):
    pass

print("\n=== 17. Diamond Problem ===")
d = D()
d.show() # Prints B (because B is first in MRO)
print(D.mro())

# 18. Slots
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

print("\n=== 18. Slots ===")
p = Point(1, 2)
# p.z = 3 # AttributeError: 'Point' object has no attribute 'z'
print("Slots saved memory by preventing dynamic attribute creation")

# =============================================================================
# BONUS
# =============================================================================

# 19. Composition
class Engine:
    def start(self): return "Engine started"

class CarWithComposition:
    def __init__(self):
        self.engine = Engine() # Has-a relationship
    
    def start(self):
        return self.engine.start()

print("\n=== 19. Composition ===")
car = CarWithComposition()
print(car.start())

# 20. Singleton
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Creating new DB connection...")
        return cls._instance

print("\n=== 20. Singleton ===")
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same object? {db1 is db2}")

# 21. Context Managers
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

print("\n=== 21. Context Manager ===")
with FileManager('test_context.txt') as f:
    f.write("Hello from context manager")
print("File closed automatically")
