# Exercises – Object-Oriented Programming (OOP)
import abc

# Helper to print section headers
def print_header(title):
    print(f"\n=== {title} ===")

# =============================================================================
# EASY LEVEL
# =============================================================================

def exercise_1():
    """
    1. Basic Class
    Create a class `Book` with attributes `title`, `author`, and `pages`. 
    Add a method `description()` that returns a formatted string like:
    "Title by Author, X pages".
    """
    print_header("Exercise 1: Basic Class")
    # Write your class here
    
    # Test your class
    pass

def exercise_2():
    """
    2. Instance Variables
    Create a `Counter` class. Each time you instantiate it, it should have 
    a `count` attribute starting at 0. Add an `increment()` method.
    """
    print_header("Exercise 2: Instance Variables")
    # Write your code here
    pass

def exercise_3():
    """
    3. Class Attributes
    Create a class `Employee` with a class attribute `company_name = "TechCorp"`. 
    Instantiate two employees and check that they share the same company name.
    """
    print_header("Exercise 3: Class Attributes")
    # Write your code here
    pass

def exercise_4():
    """
    4. Simple Inheritance
    Create a `Vehicle` parent class with a `drive()` method returning "Vroom!". 
    Create a `Car` child class that inherits from it.
    """
    print_header("Exercise 4: Simple Inheritance")
    # Write your code here
    pass

def exercise_5():
    """
    5. Method Overriding
    Create a `Cat` class and a `Dog` class. Both should have a `speak()` method, 
    but return different strings ("Meow" vs "Woof").
    """
    print_header("Exercise 5: Method Overriding")
    # Write your code here
    pass

# =============================================================================
# MEDIUM LEVEL
# =============================================================================

def exercise_6():
    """
    6. Encapsulation (Private)
    Create a `BankAccount` class. Make the `balance` attribute private (`__balance`). 
    Add `deposit(amount)` and `withdraw(amount)` methods. 
    Ensure withdraw doesn't allow taking more than the balance.
    Add `get_balance()` to access it safely.
    """
    print_header("Exercise 6: Encapsulation")
    # Write your code here
    pass

def exercise_7():
    """
    7. Constructors
    Create a `Rectangle` class. It should accept `width` and `height` in `__init__`. 
    Add an `area()` method.
    """
    print_header("Exercise 7: Constructors")
    # Write your code here
    pass

def exercise_8():
    """
    8. The __str__ Method
    Enhance the `Book` class from Exercise 1. 
    Implement `__str__` so that `print(book_object)` displays "Title by Author".
    """
    print_header("Exercise 8: Magic String Method")
    # Write your code here
    pass

def exercise_9():
    """
    9. Class Methods
    Create a `Calculator` class with a **static method** `add(a, b)` that returns 
    the sum. Show that you don't need to instantiate the class to use it.
    """
    print_header("Exercise 9: Static Method")
    # Write your code here
    pass

def exercise_10():
    """
    10. Property Decorators (Getters/Setters)
    Create a `Temperature` class. Use `@property` for `celsius`. 
    When setting celsius, ensure it's not below -273.15 (absolute zero) by raising a ValueError.
    """
    print_header("Exercise 10: Properties")
    # Write your code here
    pass

def exercise_11():
    """
    11. Inheritance with `super()`
    Create a `Person` class (name, age) and a `Student` class. 
    `Student` should inherit from `Person` and add a `student_id` in its `__init__` 
    using `super()`.
    """
    print_header("Exercise 11: Super()")
    # Write your code here
    pass

# =============================================================================
# HARD LEVEL
# =============================================================================

def exercise_12():
    """
    12. Multiple Inheritance
    Create classes `Flyable` (method `fly`) and `Swimmable` (method `swim`). 
    Create a `Duck` class that inherits from both and can both fly and swim.
    """
    print_header("Exercise 12: Multiple Inheritance")
    # Write your code here
    pass

def exercise_13():
    """
    13. Abstract Base Classes
    Use the `abc` module. Create an abstract class `Shape` with an abstract method `area()`. 
    Implement `Circle` and `Square` classes that enforce this method implementation.
    """
    print_header("Exercise 13: Abstract Base Classes")
    # Write your code here
    pass

def exercise_14():
    """
    14. Operator Overloading
    Create a `Vector` class (x, y). 
    Implement the `__add__` magic method so you can do `v3 = v1 + v2`.
    """
    print_header("Exercise 14: Operator Overloading")
    # Write your code here
    pass

def exercise_15():
    """
    15. Polymorphism Function
    Create a function `animal_sound(animal_object)` that calls `.speak()` on whatever 
    object is passed to it. Test it with Dog and Cat objects.
    """
    print_header("Exercise 15: Polymorphism")
    # Write your code here
    pass

def exercise_16():
    """
    16. Custom Exceptions
    Create a custom exception `InsufficientFundsError`.
    Create a `Wallet` class. Raise this exception if `spend(amount)` is called 
    with an amount greater than the balance.
    """
    print_header("Exercise 16: Custom Exceptions")
    # Write your code here
    pass

def exercise_17():
    """
    17. The Diamond Problem
    Create classes A, B(A), C(A), D(B, C). 
    Add a method `show()` in each that prints its name. 
    Instantiate D and call `show()`. 
    Print `D.mro()` to see the Method Resolution Order.
    """
    print_header("Exercise 17: Diamond Problem")
    # Write your code here
    pass

def exercise_18():
    """
    18. Slots (Memory Optimization)
    Create a `Point` class using `__slots__` to restrict attributes to only `x` and `y`.
    Try to assign a new attribute `z` and observe the AttributeError.
    """
    print_header("Exercise 18: Slots")
    # Write your code here
    pass

# =============================================================================
# BONUS CHALLENGES
# =============================================================================

def exercise_19():
    """
    19. Composition vs Inheritance
    Create an `Engine` class (method `start`). 
    Create a `Car` class. The `Car` should **have an** `Engine` (initialize it in constructor), 
    not inherit from it. The Car's `start()` method should delegate to the Engine's `start()`.
    """
    print_header("Exercise 19: Composition")
    # Write your code here
    pass

def exercise_20():
    """
    20. Singleton Pattern
    Implement a `DatabaseConnection` class that allows only ONE instance to ever be created.
    Override `__new__` to achieve this.
    """
    print_header("Exercise 20: Singleton")
    # Write your code here
    pass

def exercise_21():
    """
    21. Context Managers
    Create a class `FileManager` that implements `__enter__` and `__exit__`. 
    Use it with the `with` statement to open and automatically close a file.
    """
    print_header("Exercise 21: Context Managers")
    # Write your code here
    pass

if __name__ == '__main__':
    # You can call specific exercises here to test your solutions
    exercise_1()
    print("\nRun specific examples by calling the functions above!")
