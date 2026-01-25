# Comprehensive Loop Examples

# ==========================================
# 1. Basic Iteration (For Loops)
# ==========================================
names = ["Alice", "Bob", "Charlie"]

# Iterating over a list
print("--- List Iteration ---")
for name in names:
    print(f"Hello, {name}")

# Iterating with index using enumerate() (Pythonic)
print("\n--- Enumerate ---")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# Iterating over range()
print("\n--- Range ---")
for i in range(0, 10, 2): # Start 0, Stop 10 (exclusive), Step 2
    print(i, end=" ")
print()

# ==========================================
# 2. While Loops & Input Validation
# ==========================================
print("\n--- While Loop ---")
count = 3
while count > 0:
    print(f"Counting down: {count}")
    count -= 1

# Input validation pattern (simulated)
# while True:
#     age = input("Enter age: ")
#     if age.isdigit():
#         break
#     print("Invalid, try again.")

# ==========================================
# 3. Loop Control Statements
# ==========================================
print("\n--- Break, Continue, Else ---")
for i in range(10):
    if i == 3:
        print("Skipping 3 (continue)")
        continue
    if i == 8:
        print("Breaking at 8")
        break
    print(i, end=" ")
else:
    # Runs ONLY if loop completes without break
    print("Loop finished normally") 
print()

# ==========================================
# 4. Dictionary Iteration
# ==========================================
print("\n--- Dictionary Iteration ---")
scores = {"Alice": 95, "Bob": 87}

# Keys (default)
for name in scores:
    print(f"Key: {name}")

# Values
for score in scores.values():
    print(f"Value: {score}")

# Key-Value pairs
for name, score in scores.items():
    print(f"{name}: {score}")

# ==========================================
# 5. Zip (Parallel Iteration)
# ==========================================
print("\n--- Zip ---")
people = ["Alice", "Bob"]
ages = [25, 30]

for p, a in zip(people, ages):
    print(f"{p} is {a} years old")
