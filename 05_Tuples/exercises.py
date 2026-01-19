# Exercises – Tuples
# Fill in the code blocks below to solve the exercises.

# ==========================================
# Easy
# ==========================================

def exercise_1():
    """
    1. Create a tuple with three different data types (e.g., int, string, float).
    2. Print each element separately.
    """
    # Write your code here
    pass

def exercise_2(a, b):
    """
    Write a function that accepts two numbers `a` and `b`.
    Return both the sum (a+b) and the product (a*b) as a single tuple.
    """
    # Write your code here
    pass

def exercise_3():
    """
    Create a tuple (10, 20, 30, 40, 50).
    Print the last element using negative indexing.
    """
    # Write your code here
    pass


# ==========================================
# Medium
# ==========================================

def exercise_4(nums):
    """
    Given a list of numbers, convert it to a tuple.
    Return True if the tuple contains duplicates, otherwise False.
    """
    # Write your code here
    pass

def exercise_5():
    """
    Create a tuple representing a date: (2023, 10, 25).
    Unpack it into three variables: year, month, day.
    Print the variables.
    """
    # Write your code here
    pass

def exercise_6():
    """
    Create a dictionary called `locations`.
    Use a tuple (latitude, longitude) as a key, and a string (city name) as the value.
    Add one entry ex: (40.7, -74.0) -> "New York"
    Print the city name by accessing it with the coordinate tuple.
    """
    # Write your code here
    pass


# ==========================================
# Hard
# ==========================================

def exercise_7(*iterables, fillvalue=None):
    """
    Implement a function `zip_longest_tuple` that behaves like itertools.zip_longest.
    It should take multiple iterables and return a tuple of tuples.
    If iterables are strictly uneven, use `fillvalue` to fill missing spots.
    Example: zip_longest_tuple([1,2], [3], fillvalue=None) -> ((1, 3), (2, None))
    """
    # Write your code here
    pass

def exercise_8(nested_tuple):
    """
    Write a recursive function that flattens a nested tuple of arbitrary depth into a single flat tuple.
    Example: ((1, 2), (3, (4,))) -> (1, 2, 3, 4)
    """
    # Write your code here
    pass

def exercise_9():
    """
    Create a GENERATOR EXPRESSION that calculates squares of numbers 0 to 9.
    Immediately convert this generator into a tuple and return/print it.
    """
    # Write your code here
    pass

class ImmutableStack:
    """
    10. Design a simple immutable stack class using a tuple for internal storage.
    Methods:
      - push(item): Returns a NEW ImmutableStack with item added.
      - pop(): Returns a tuple (top_item, new_stack).
      - peek(): Returns the top item.
      - __init__(self, data=()): Initialize with a tuple.
    """
    def __init__(self, data=()):
        self._data = data

    def push(self, item):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

if __name__ == "__main__":
    # Test your functions here
    pass
