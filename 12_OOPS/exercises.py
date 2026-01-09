# Exercises – Object-Oriented Programming

## Easy Level

### 1. Basic Class
Create a class `Book` with attributes `title`, `author`, and `pages`. Add a method `description()` that returns a formatted string.

### 2. Instance Variables
Create a `Counter` class. Each time you instantiate it, it should have a `count` attribute starting at 0. Add an `increment()` method.

### 3. Class Attributes
Create a class `Employee` with a class attribute `company_name = "TechCorp"`. Instantiate two employees and check their company name.

### 4. Simple Inheritance
Create a `Vehicle` parent class with a `drive()` method. Create a `Car` child class that inherits from it.

### 5. Method Overriding
Create a `Cat` class and a `Dog` class. Both should have a `speak()` method, but return different strings ("Meow" vs "Woof").

## Medium Level

### 6. Encapsulation (Private)
Create a `BankAccount` class. Make the `balance` attribute private (`__balance`). Add `deposit()` and `withdraw()` methods.

### 7. Constructors
Create a `Rectangle` class. It should accept `width` and `height` in `__init__`. Add an `area()` method.

### 8. The __str__ Method
Enhance the `Book` class from Exercise 1. When you `print(book_object)`, it should display "Title by Author".

### 9. Class Methods
Create a `Calculator` class with a **static method** `add(a, b)` that returns the sum. You shouldn't need to instantiate the class to use it.

### 10. Property Decorators
Create a `Temperature` class. Use `@property` for `celsius`. When setting celsius, ensure it's not below -273.15 (absolute zero).

### 11. Inheritance with Super
Create a `Person` class (name, age) and a `Student` class. `Student` should inherit from `Person` and add a `student_id` in its `__init__` using `super()`.

## Hard Level

### 12. Multiple Inheritance
Create classes `Flyable` (method `fly`) and `Swimmable` (method `swim`). Create a `Duck` class that inherits from both.

### 13. Abstract Base Classes
Use `abc` module. Create an abstract class `Shape` with an abstract method `area()`. Implement `Circle` and `Square` classes that enforce this method.

### 14. Operator Overloading
Create a `Vector` class (x, y). Implement the `__add__` magic method so you can do `v1 + v2`.

### 15. Polymorphism
Create a function `animal_sound(animal_object)` that calls `.speak()` on whatever object is passed (Dog, Cat, etc.).

### 16. Custom Exceptions
Create a class `wallet`. Raise a custom `InsufficientFundsError` if trying to withdraw more than the current balance.

### 17. The Diamond Problem
Create classes A, B(A), C(A), D(B, C). Add a method `show()` in each. Instantiate D and call `show()`. Inspect `D.mro()`.

### 18. Slots
Create a `Point` class using `__slots__` to restrict attributes to only `x` and `y` for memory optimization.

## Bonus Challenges

### 19. Composition
Create an `Engine` class and a `Car` class. The `Car` should **have an** `Engine` (not inherit from it). This is "Has-a" vs "Is-a" relationship.

### 20. Singleton Pattern
Implement a `DatabaseConnection` class that allows only ONE instance to ever be created (Singleton pattern).

### 21. Context Managers
Create a class `FileManager` that implements `__enter__` and `__exit__`. Use it with the `with` statement.

**See `solutions.py` for complete solutions!**
