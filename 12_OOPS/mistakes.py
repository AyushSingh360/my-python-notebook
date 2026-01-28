# Common Beginner Mistakes in Object-Oriented Programming

# ==========================================
# Mistake 1: Forgetting 'self' in method definition
# ==========================================
# Incorrect:
# class Dog:
#     def bark():  # TypeError when called on instance
#         print("Woof")
#
# Fixed:
class Dog:
    def bark(self): # Must include self!
        print("Woof")


# ==========================================
# Mistake 2: Using Mutable Class Attributes
# ==========================================
# Incorrect:
# class Backpack:
#     items = [] # Shared by ALL instances!
#
# p1 = Backpack()
# p2 = Backpack()
# p1.items.append("Apple")
# print(p2.items) # ['Apple'] - Unexpected!
#
# Fixed:
class Backpack:
    def __init__(self):
        self.items = [] # Unique to each instance


# ==========================================
# Mistake 3: Assigning to method instead of calling it
# ==========================================
class Cat:
    def meow(self):
        print("Meow")

c = Cat()
# Incorrect:
# c.meow = 5 # Overwrites the method with an integer!
# c.meow() # TypeError: 'int' object is not callable
#
# Fixed:
c.meow() # Call with parentheses


# ==========================================
# Mistake 4: Forgetting super().__init__()
# ==========================================
class Parent:
    def __init__(self):
        self.data = "Important Data"

class Child(Parent):
    def __init__(self):
        # self.extra = "Extra" # Missing super().__init__()
        pass

c = Child()
# print(c.data) # AttributeError: 'Child' object has no attribute 'data'

# Fixed:
class ChildFixed(Parent):
    def __init__(self):
        super().__init__() # Initializes parent attributes
        self.extra = "Extra"


# ==========================================
# Mistake 5: Confusing 'is' vs '=='
# ==========================================
a = [1, 2, 3]
b = [1, 2, 3]
print(f"a == b: {a == b}") # True (Values are equal)
print(f"a is b: {a is b}") # False (Different objects in memory)
# 'is' checks for identity (same memory address)
# '==' checks for equality (same content)
