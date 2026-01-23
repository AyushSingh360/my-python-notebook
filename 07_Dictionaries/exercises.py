# Exercises – Dictionaries
# Fill in the code blocks below to solve the exercises.

# ==========================================
# Easy
# ==========================================

def exercise_1():
    """
    1. Create a dictionary representing a book with these keys:
       - title: "The Hobbit"
       - author: "J.R.R. Tolkien"
       - pages: 310
    2. Print the author's name accessed from the dictionary.
    """
    # Write your code here
    pass

def exercise_2(book_dict):
    """
    Given the book dictionary from Exercise 1:
    1. Add a new key `year` with the value 1937.
    2. Return the updated dictionary.
    """
    # Write your code here
    pass

def exercise_3(book_dict):
    """
    Given the book dictionary:
    1. Try to retrieve the value for the key `publisher`.
    2. Use .get() to return "Unknown" if the key doesn't exist.
    """
    # Write your code here
    pass


# ==========================================
# Medium
# ==========================================

def exercise_4(d):
    """
    Write a function `invert_dict(d)` that swaps keys and values.
    Assume all values in `d` are unique and hashable.
    Example: {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    """
    # Write your code here
    pass

def exercise_5(names):
    """
    Given a list of names, build a dictionary mapping each name to a unique ID.
    IDs should start from 1000 and increment by 1 for each name.
    Example: ["Alice", "Bob"] -> {"Alice": 1000, "Bob": 1001}
    """
    # Write your code here
    pass

def exercise_6(d1, d2):
    """
    Merge dictionary `d2` into `d1` such that `d2` overrides `d1` keys.
    Do not change `d1` in-place; return a NEW merged dictionary.
    Use the `|` operator (Python 3.9+) or `.copy()` + `.update()`.
    """
    # Write your code here
    pass


# ==========================================
# Hard
# ==========================================

class KVStore:
    """
    7. Implement a simple Key-Value store class.
    Methods:
      - set(key, value): Stores the value.
      - get(key): Returns the value, or None if not found.
      - delete(key): Removes the key if it exists (no error if missing).
    """
    def __init__(self):
        pass

    def set(self, key, value):
        pass

    def get(self, key):
        pass

    def delete(self, key):
        pass

def exercise_8(nested_dict):
    """
    Write a function that flattens a nested dictionary (one level deep) into `key.subkey` format.
    Example: {"a": {"x": 1}, "b": 2} -> {"a.x": 1, "b": 2}
    """
    # Write your code here
    pass

def exercise_9():
    """
    Using a DICT COMPREHENSION, create a mapping of numbers 1 to 5 to their factorial.
    Example keys: 1, 2, 3, 4, 5
    """
    # Write your code here
    pass

def exercise_10(rows, column, value):
    """
    Simulate a basic SQL "SELECT * FROM table WHERE column=value".
    - `rows`: A list of dictionaries.
    - `column`: The key to check.
    - `value`: The value to match.
    Return a list of matching row dictionaries.
    """
    # Write your code here
    pass

if __name__ == "__main__":
    # Test your functions here
    pass
