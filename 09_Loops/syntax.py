# Basic loop syntax examples

# while loop
i = 5
while i > 0:
    print(i)
    i -= 1

# for loop
for x in range(3):
    print(x)

# break / continue
for x in range(5):
    if x == 2: continue
    if x == 4: break
    print(x)
