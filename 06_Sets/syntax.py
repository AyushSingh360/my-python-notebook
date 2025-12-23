# Basic set syntax examples
evens = {2, 4, 6}
odds = set([1, 3, 5])
print(evens)
print(odds)
# Add / remove
evens.add(8)
evens.discard(4)
# Set operations
union = evens | odds
intersection = evens & odds
difference = evens - odds
print("union", union)
print("intersection", intersection)
print("difference", difference)
