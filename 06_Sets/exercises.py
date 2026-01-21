# Exercises – Sets
# Fill in the code blocks below to solve the exercises.

# ==========================================
# Easy
# ==========================================

def exercise_1(raw_list):
    """
    1. Convert the list `[1, 2, 2, 3, 3, 3]` into a set.
    2. Return the set.
    """
    # Write your code here
    pass

def exercise_2(word):
    """
    Check if the given word contains the letter 'y' using a set.
    Return True if it does, False otherwise.
    """
    # Write your code here
    pass

def exercise_3():
    """
    1. Create a set of the first five natural numbers {1, 2, 3, 4, 5}.
    2. Add the number 6 to it.
    3. Return the modified set.
    """
    # Write your code here
    pass


# ==========================================
# Medium
# ==========================================

def exercise_4(list1, list2):
    """
    Given two lists of student IDs, find the IDs that appear in BOTH lists.
    Return the result as a set.
    """
    # Write your code here
    pass

def exercise_5(s):
    """
    Write a function that returns a set of unique characters in the string `s`.
    Spaces and punctuation should be included if present.
    """
    # Write your code here
    pass

def exercise_6():
    """
    Using a SET COMPREHENSION, generate all even numbers between 1 and 20 (inclusive).
    Return the resulting set.
    """
    # Write your code here
    pass


# ==========================================
# Hard
# ==========================================

def exercise_7(words, dictionary):
    """
    Implement a simple spell-checker.
    Given a list of `words` and a list of correct words `dictionary`:
    1. Convert `dictionary` to a set for O(1) lookups.
    2. Return a list of words from the input `words` that are NOT in the dictionary.
    """
    # Write your code here
    pass

def exercise_8(s):
    """
    Write a function that returns the POWER SET of a given set `s`.
    The power set is the set of all subsets of s (including empty set and s itself).
    Since sets cannot contain other sets, return a set of FROZENSETs.
    Example: {1, 2} -> {frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})}
    """
    # Write your code here
    pass

def exercise_9(sentences):
    """
    Given a list of sentences, build a set of all distinct words.
    - Case-insensitive (treat 'The' and 'the' as same).
    - Strip punctuation like .,!?"'
    - Return the set of clean words.
    """
    # Write your code here
    pass

def exercise_10(records, fields):
    """
    Simulate a relational SELECT operation (projection).
    Input:
      - records: A list of dictionaries (rows).
      - fields: A set of field names (columns) to keep.
    Output:
      - A set of tuples, where each tuple contains the values of the requested fields for a row.

    Example:
      records = [{"id":1, "name":"A"}, {"id":2, "name":"B"}]
      fields = {"id"}
      result -> {(1,), (2,)}
    """
    # Write your code here
    pass

if __name__ == "__main__":
    # Test your functions here
    pass
