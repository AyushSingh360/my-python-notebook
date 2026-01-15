# Solutions – Lists

# ==========================================
# Easy
# ==========================================

# 1. Create list and access element
# ------------------------------------------
# We create a list using square brackets.
numbers = [1, 2, 3, 4, 5]
# Lists are 0-indexed, so the third element is at index 2.
print(f"3rd element: {numbers[2]}") 


# 2. Append and Print
# ------------------------------------------
words = ["start"]
words.append("end") # Modifies the list in-place
print(f"Appended list: {words}")


# 3. Sum of List
# ------------------------------------------
nums_to_sum = [3, 6, 9, 12]
total = sum(nums_to_sum) # Built-in function sum() is efficient
print(f"Sum: {total}")


# ==========================================
# Medium
# ==========================================

# 4. Remove Duplicates (Preserving Order)
# ------------------------------------------
def remove_duplicates(seq):
    seen = set() # O(1) lookups
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(f"Unique ordered: {remove_duplicates([1, 2, 2, 3, 1, 4])}")


# 5. Squares of Odd Numbers (List Comprehension)
# ------------------------------------------
input_nums = [1, 2, 3, 4, 5, 6, 7]
# Logic: [ transform(x) for x in iterable if condition ]
odd_squares = [x**2 for x in input_nums if x % 2 != 0]
print(f"Odd squares: {odd_squares}")


# 6. Rotate List
# ------------------------------------------
def rotate(lst, k):
    if not lst: return lst
    n = len(lst)
    k %= n # Handle k > n
    # Slice the last k elements and put them at the start
    return lst[-k:] + lst[:-k]

print(f"Rotated: {rotate([1, 2, 3, 4, 5], 2)}")


# ==========================================
# Hard
# ==========================================

# 7. Simple Queue Implementation
# ------------------------------------------
class SimpleQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item) # Add to end
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) # Remove from front (Inefficient for large lists!)
        return None
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None
        
    def is_empty(self):
        return len(self.queue) == 0

q = SimpleQueue()
q.enqueue('a'); q.enqueue('b')
print(f"Dequeued: {q.dequeue()}")
print(f"Next in line: {q.peek()}")


# 8. Longest Increasing Subsequence
# ------------------------------------------
# This is a classic Dynamic Programming problem O(n^2)
def length_of_lis(nums):
    if not nums: return 0
    
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

lis_input = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"LIS Length: {length_of_lis(lis_input)}")


# 9. 3-letter strings (Cross Product)
# ------------------------------------------
# Nested loops equivalent:
# for a in 'abc': for b in 'abc': for c in 'abc': ...
chars = ['a', 'b', 'c']
triples = [x+y+z for x in chars for y in chars for z in chars]
print(f"First 5 triples: {triples[:5]}")


# 10. FizzBuzz Comprehension
# ------------------------------------------
# Order matters! Check 15 first.
fizzbuzz = [
    "FizzBuzz" if i % 15 == 0 else 
    "Fizz" if i % 3 == 0 else 
    "Buzz" if i % 5 == 0 else 
    str(i) 
    for i in range(1, 101)
]
print(f"FizzBuzz first 15: {fizzbuzz[:15]}")
