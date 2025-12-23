# Examples demonstrating tuple usage

# 1. Returning multiple values from a function

def min_max(nums):
    return (min(nums), max(nums))

values = [4, 2, 9, 5]
low, high = min_max(values)
print("Low:", low, "High:", high)

# 2. Using a tuple as a dictionary key
location = {(40.7128, -74.0060): "New York"}
print(location[(40.7128, -74.0060)])

# 3. Tuple unpacking with *rest
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first, middle, last)

# 4. Nested tuples
nested = ((1, 2), (3, 4))
print(nested[1][0])
