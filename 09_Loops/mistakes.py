# Common Beginner Mistakes with Loops

# ==========================================
# Mistake 1: Infinite Loop
# ==========================================
# Forgetting to update the loop variable in a while loop.

# INCORRECT:
# i = 0
# while i < 5:
#     print(i)
#     # i never changes!

# CORRECT:
i = 0
while i < 5:
    print(i)
    i += 1


# ==========================================
# Mistake 2: Modifying List While Iterating
# ==========================================
# Removing/adding items changes indices, causing skips or crashes.

numbers = [1, 2, 3, 4, 5]

# INCORRECT:
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num) 
# Result: Skips checking elements after removal

# CORRECT: Iterate over a COPY
for num in numbers[:]: # [:] creates a shallow copy
    if num % 2 == 0:
        numbers.remove(num)
print(f"Filtered: {numbers}")


# ==========================================
# Mistake 3: Range Off-By-One
# ==========================================
# Thinking range(n) includes n.

# INCORRECT:
# for i in range(1, 5): 
#     print(i) # Prints 1, 2, 3, 4 (stops BEFORE 5)

# CORRECT:
for i in range(1, 6):
    print(i) # Prints 1, 2, 3, 4, 5


# ==========================================
# Mistake 4: Misusing For-Else
# ==========================================
# Expecting 'else' to run when 'break' happens.
# Actually, 'else' runs only if the loop finishes NORMALLY (no break).

def contains_target(lst, target):
    for item in lst:
        if item == target:
            print("Found it!")
            break
    else:
        # Runs if loop completes without hitting 'break'
        print("Not found")

contains_target([1, 2, 3], 99)


# ==========================================
# Mistake 5: Iterating by index unnecessarily
# ==========================================
fruits = ["apple", "banana"]

# INCORRECT (Non-Pythonic):
for i in range(len(fruits)):
    print(fruits[i])

# CORRECT:
for fruit in fruits:
    print(fruit)

# If index is needed:
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
