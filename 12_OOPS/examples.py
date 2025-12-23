# Examples demonstrating OOP concepts

# 1. Class vs Instance Variables
class Counter:
    count = 0  # Class variable
    def __init__(self):
        Counter.count += 1
        self.my_count = 0  # Instance variable

a = Counter()
b = Counter()
print(Counter.count)  # 2

# 2. Encapsulation (Private members)
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private
    def deposit(self, amt):
        self.__balance += amt
    def get_balance(self):
        return self.__balance

acc = Account(100)
acc.deposit(50)
print(acc.get_balance())
# print(acc.__balance)  # AttributeError

# 3. Polymorphism
class Cat:
    def speak(self): print("Meow")
class Dog:
    def speak(self): print("Woof")

for animal in [Cat(), Dog()]:
    animal.speak()
