# Examples demonstrating loops

# 1. Sum numbers 1-100
total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)

# 2. Iterate list
names = ["Alice", "Bob"]
for name in names:
    print("Hello", name)

# 3. Search with break/else
found = False
for i in range(5):
    if i == 3:
        print("Found 3")
        found = True
        break
if not found:
    print("Not found")

# 4. Nested loops (multiplication table)
for r in range(1, 4):
    for c in range(1, 4):
        print(f"{r}*{c}={r*c}", end=" ")
    print()
