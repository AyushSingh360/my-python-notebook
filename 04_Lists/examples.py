# Examples demonstrating list operations

# 1. Create a mixed‑type list
mixed = [42, "answer", 3.14, True]
print(mixed)

# 2. Indexing and negative indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # apple
print(fruits[-1])     # cherry

# 3. Slicing
print(fruits[1:])     # ['banana', 'cherry']
print(fruits[:2])     # ['apple', 'banana']

# 4. Modifying elements
fruits[1] = "blueberry"
print(fruits)

# 5. Adding elements
fruits.append("date")
fruits.insert(0, "avocado")
print(fruits)

# 6. Removing elements
fruits.remove("blueberry")
removed = fruits.pop()
print("popped", removed)
print(fruits)

# 7. List comprehension – even numbers up to 10
evens = [i for i in range(11) if i % 2 == 0]
print(evens)

# 8. Sorting and reversing
nums = [5, 2, 9, 1]
nums.sort()
print(nums)
nums.reverse()
print(nums)
