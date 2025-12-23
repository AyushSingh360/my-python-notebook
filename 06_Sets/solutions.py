# Solutions – Sets

# 1. List to set
lst = [1,2,2,3,3,3]
print(set(lst))  # {1, 2, 3}

# 2. Letter membership using set
word = "python"
print('y' in set(word))  # True

# 3. Add element to set
nums = {1,2,3,4,5}
nums.add(6)
print(nums)

# 4. Intersection of two ID lists
list1 = [101,102,103,104]
list2 = [103,104,105]
common_ids = set(list1) & set(list2)
print(common_ids)  # {103, 104}

# 5. Unique characters
def unique_chars(s):
    return set(s)
print(unique_chars("hello"))

# 6. Even numbers 1‑20 via set comprehension
evens = {x for x in range(1,21) if x % 2 == 0}
print(evens)

# 7. Simple spell‑checker
def misspelled(words, dictionary):
    dict_set = set(dictionary)
    return [w for w in words if w not in dict_set]
words = ["apple", "bananna", "cherry"]
dictionary = ["apple", "banana", "cherry"]
print(misspelled(words, dictionary))  # ['bananna']

# 8. Power set
def power_set(s):
    lst = list(s)
    n = len(lst)
    result = set()
    for i in range(1 << n):
        subset = frozenset(lst[j] for j in range(n) if i & (1 << j))
        result.add(subset)
    return result
print(power_set({1,2}))

# 9. Distinct words from sentences
def distinct_words(sentences):
    words = set()
    for sent in sentences:
        for w in sent.lower().split():
            words.add(w.strip('.,!?"\''))
    return words
print(distinct_words(["Hello world!", "Python is great."]))

# 10. SELECT projection
def select_projection(records, fields):
    return {tuple(rec[f] for f in fields) for rec in records}
records = [{"id":1,"n":"A"}, {"id":2,"n":"B"}]
print(select_projection(records, {"id"}))
