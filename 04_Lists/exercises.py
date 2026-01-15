# Exercises – Lists
# Fill in the code blocks below to solve the exercises.

# ==========================================
# Easy
# ==========================================

def exercise_1():
    """
    1. Create a list of the first five natural numbers (1, 2, 3, 4, 5).
    2. Print the third element.
    """
    # Write your code here
    pass

def exercise_2():
    """
    1. Create a list containing the string "start".
    2. Append the string "end" to the list.
    3. Print the final list.
    """
    # Write your code here
    pass

def exercise_3():
    """
    Compute and print the sum of all numbers in the list [3, 6, 9, 12].
    """
    # Write your code here
    pass


# ==========================================
# Medium
# ==========================================

def exercise_4(input_list):
    """
    Write a function that removes duplicates from a list while preserving the original order.
    Example: [1, 2, 2, 3, 1, 4] -> [1, 2, 3, 4]
    """
    # Write your code here
    pass

def exercise_5(numbers):
    """
    Given a list of integers, produce a new list containing only the squares of the odd numbers.
    Use List Comprehension.
    """
    # Write your code here
    pass

def exercise_6(lst, k):
    """
    Implement a function that rotates the list to the right by `k` positions.
    Example: rotate([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
    """
    # Write your code here
    pass


# ==========================================
# Hard
# ==========================================

class SimpleQueue:
    """
    7. Simulate a simple queue using a list by implementing the following methods:
       - enqueue(item): Add an item to the queue.
       - dequeue(): Remove and return the front item.
       - peek(): Return the front item without removing it.
       - is_empty(): Return True if the queue is empty.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass

def exercise_8(arr):
    """
    Write a function that finds the LENGTH of the longest increasing subsequence in a list of integers.
    Example: [10, 9, 2, 5, 3, 7, 101, 18] -> 4 (The subsequence is [2, 3, 7, 18])
    """
    # Write your code here
    pass

def exercise_9():
    """
    Create a list comprehension that generates all 3-letter strings from the alphabet 'a' through 'c'.
    Example: 'aaa', 'aab', ..., 'ccc'
    """
    # Write your code here
    pass

def exercise_10():
    """
    Implement the "FizzBuzz" problem using a single list comprehension for numbers 1 to 100.
    - multiples of 3 -> "Fizz"
    - multiples of 5 -> "Buzz"
    - multiples of 15 -> "FizzBuzz"
    - otherwise -> number
    """
    # Write your code here
    pass

if __name__ == "__main__":
    # You can test your functions here
    print("Run these exercises by calling the functions!")
