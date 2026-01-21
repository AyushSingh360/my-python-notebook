# Solutions – Sets

# ==========================================
# Easy
# ==========================================

# 1. List to Set
# ------------------------------------------
def exercise_1(raw_list):
    # set() constructor removes duplicates
    return set(raw_list)

print(f"Set from list: {exercise_1([1, 2, 2, 3, 3, 3])}")


# 2. Check for char in word
# ------------------------------------------
def exercise_2(word):
    # Converting to set makes "in" check O(1) instead of O(n)
    return 'y' in set(word)

print(f"Has 'y' in python? {exercise_2('python')}")


# 3. Modify Set
# ------------------------------------------
def exercise_3():
    s = {1, 2, 3, 4, 5}
    s.add(6)
    return s

print(f"Added 6: {exercise_3()}")


# ==========================================
# Medium
# ==========================================

# 4. Intersection of IDs
# ------------------------------------------
def exercise_4(list1, list2):
    # Convert both to sets and use intersection (&) operator
    return set(list1) & set(list2)

print(f"Common IDs: {exercise_4([101, 102], [102, 103])}")


# 5. Unique Characters
# ------------------------------------------
def exercise_5(s):
    return set(s)

print(f"Unique chars in 'hello': {exercise_5('hello')}")


# 6. Set Comprehension (Evens)
# ------------------------------------------
def exercise_6():
    # { expr for item in iterable if condition }
    return {x for x in range(1, 21) if x % 2 == 0}

print(f"Evens 1-20: {exercise_6()}")


# ==========================================
# Hard
# ==========================================

# 7. Spell Checker
# ------------------------------------------
def exercise_7(words, dictionary):
    # O(1) lookup set
    dict_set = set(dictionary)
    # Check each word against dict_set
    return [w for w in words if w not in dict_set]

words_input = ["apple", "bananna", "cherry"]
correct_dict = ["apple", "banana", "cherry"]
print(f"Misspelled: {exercise_7(words_input, correct_dict)}")


# 8. Power Set (Set of Frozensets)
# ------------------------------------------
def exercise_8(s):
    # Convert to list to index elements
    elements = list(s)
    n = len(elements)
    power_set = set()
    
    # Iterate from 0 to 2^n - 1  (binary representation approach)
    for i in range(1 << n):
        subset = []
        for j in range(n):
            # Check if j-th bit is set
            if (i >> j) & 1:
                subset.append(elements[j])
        power_set.add(frozenset(subset))
        
    return power_set

print(f"Power set of {{1, 2}}: {exercise_8({1, 2})}")


# 9. Distinct Words
# ------------------------------------------
def exercise_9(sentences):
    distinct = set()
    for sentence in sentences:
        # Normalize: lower case
        words = sentence.lower().split()
        for word in words:
            # Strip punctuation
            clean_word = word.strip('.,!?"\'')
            if clean_word:
                distinct.add(clean_word)
    return distinct

text = ["Hello world!", "Python is great.", "Hello python."]
print(f"Distinct words: {exercise_9(text)}")


# 10. SELECT Projection
# ------------------------------------------
def exercise_10(records, fields):
    # Set comprehension to build set of tuples
    return {
        tuple(record[f] for f in fields) # generator expr inside tuple()
        for record in records
    }

data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 1, "name": "Alice", "age": 30} # Duplicate row effectively
]
cols = {"name", "age"}
print(f"Projected unique rows: {exercise_10(data, cols)}")
