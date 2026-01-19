# Solutions – Tuples

# ==========================================
# Easy
# ==========================================

# 1. Create tuple with mixed types
# ------------------------------------------
# Just separate by commas.
mixed = (42, "hello", 3.14)
print(f"Element 1: {mixed[0]}")
print(f"Element 2: {mixed[1]}")
print(f"Element 3: {mixed[2]}")


# 2. Sum and Product Tuple
# ------------------------------------------
# Returning multiple values is idiomatic Python (it actually returns a tuple)
def calculate_stats(a, b):
    sum_val = a + b
    prod_val = a * b
    return (sum_val, prod_val) # Parentheses optional here, but good for clarity

result = calculate_stats(5, 10)
print(f"Sum: {result[0]}, Product: {result[1]}")


# 3. Negative Indexing
# ------------------------------------------
my_nums = (10, 20, 30, 40, 50)
print(f"Last element: {my_nums[-1]}")


# ==========================================
# Medium
# ==========================================

# 4. Check for Duplicates
# ------------------------------------------
def check_duplicates(nums):
    # Convert list to tuple (as requested)
    t = tuple(nums)
    # Compare length of set (unique items) with length of tuple
    return len(set(t)) != len(t)

print(f"Duplicates in [1, 2, 2]: {check_duplicates([1, 2, 2])}")
print(f"Duplicates in [1, 2, 3]: {check_duplicates([1, 2, 3])}")


# 5. Unpacking Date
# ------------------------------------------
date_tuple = (2025, 12, 25)
year, month, day = date_tuple # Unpacking
print(f"Year: {year}, Month: {month}, Day: {day}")


# 6. Tuple as Dictionary Key
# ------------------------------------------
# This works because tuples are hashable (immutable)
locations = {}
# Key: (Lat, Long) Tuple
coord = (40.7, -74.0)
locations[coord] = "New York"

print(f"City at {coord}: {locations[coord]}")


# ==========================================
# Hard
# ==========================================

# 7. zip_longest_tuple
# ------------------------------------------
def zip_longest_tuple(*iterables, fillvalue=None):
    # Find the length of the longest iterable
    max_len = max(len(it) for it in iterables)
    
    result = []
    for i in range(max_len):
        row = []
        for it in iterables:
            # If current iterable has data at i, use it, else use fillvalue
            if i < len(it):
                row.append(it[i])
            else:
                row.append(fillvalue)
        result.append(tuple(row)) # Convert inner list to tuple
    
    return tuple(result) # Convert outer list to tuple

print(f"Zipped: {zip_longest_tuple([1, 2], [3], fillvalue=None)}")
# Output: ((1, 3), (2, None))


# 8. Recursive Flatten
# ------------------------------------------
def flatten(nested):
    flat_list = []
    for item in nested:
        if isinstance(item, tuple):
            # extend by recursively calling flatten
            # Note: flatten returns a tuple, so we convert to list to extend efficiently or just use +=
            # Let's do it purely with tuples for elegance (less efficient though)
            pass 
        else:
            pass
            
    # Better implementation for tuple concatenation
    result = ()
    for item in nested:
        if isinstance(item, tuple):
            result += flatten(item)
        else:
            result += (item,)
    return result

nested = ((1, 2), (3, (4, 5)))
print(f"Flattened: {flatten(nested)}")


# 9. Generator Expression to Tuple
# ------------------------------------------
# A generator expression is like a list comprehension but with parentheses
gen = (x**2 for x in range(10))
# Convert to tuple to realize the values
squares_tuple = tuple(gen)
print(f"Squares: {squares_tuple}")


# 10. Immutable Stack
# ------------------------------------------
class ImmutableStack:
    def __init__(self, data=()):
        self._data = tuple(data) # Ensure it's a tuple
        
    def push(self, item):
        # Return a NEW stack with the new item appended
        return ImmutableStack(self._data + (item,))
        
    def pop(self):
        if not self._data:
            return None, self # Or raise Error
        # Return top item, and a NEW stack without that item
        top = self._data[-1]
        new_data = self._data[:-1]
        return top, ImmutableStack(new_data)
        
    def peek(self):
        if not self._data: 
            return None
        return self._data[-1]

    def __repr__(self):
        return f"Stack{self._data}"

# Usage
s0 = ImmutableStack()
s1 = s0.push(10)
s2 = s1.push(20)
print(f"Stack 2: {s2}")
val, s3 = s2.pop()
print(f"Popped: {val}, Remaining: {s3}")
