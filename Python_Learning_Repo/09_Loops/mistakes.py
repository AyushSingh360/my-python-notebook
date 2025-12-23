# Common beginner mistakes for Loops

# Mistake 1 – Infinite loop (forgetting to update condition)
# Incorrect
# i = 0
# while i < 5: print(i)
# Fixed
i = 0
while i < 5:
    print(i)
    i += 1

# Mistake 2 – Modifying list while iterating
# Incorrect
# lst = [1, 2]
# for x in lst: lst.remove(x)
# Fixed – iterate copy
lst = [1, 2]
for x in lst[:]:
    lst.remove(x)

# Mistake 3 – Misunderstanding for-else (else runs if NO break)
# Incorrect expectation that else runs on break
# for x in range(3):
#     if x==1: break
# else:
#     print("Done")   # won't run
