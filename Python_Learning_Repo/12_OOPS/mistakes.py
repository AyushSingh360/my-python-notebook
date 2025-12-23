# Common beginner mistakes for OOP

# Mistake 1 – Forgetting self
# Incorrect
# class C:
#     def method(): ... 
# Fixed
class C:
    def method(self):
        pass

# Mistake 2 – Using mutable class variable for instance data
# Incorrect
# class Item:
#     tags = []  # Shared by all instances!
# Fixed
class Item:
    def __init__(self):
        self.tags = []

# Mistake 3 – Calling methods without parentheses
# Incorrect
# d.bark   # function object, doesn't execute
# Fixed
# d.bark()
