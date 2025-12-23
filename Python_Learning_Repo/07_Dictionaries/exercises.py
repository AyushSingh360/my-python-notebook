# Exercises – Dictionaries

**Easy**
1. Create a dictionary representing a book with keys `title`, `author`, `pages`. Print the author.
2. Add a new key `year` with a value of your choice.
3. Retrieve a key `publisher` using `.get()` with a default value "Unknown".

**Medium**
4. Write a function `invert_dict(d)` that swaps keys and values (assume values are unique).
5. Given a list of names, build a dictionary mapping each name to a unique ID starting from 1000.
6. Merge two dictionaries such that the second overrides the first, without using the `|` operator (use `.update()` or `**`).

**Hard**
7. Implement a simple key‑value store class with `set`, `get`, `delete` methods.
8. Write a function that flattens a nested dictionary (one level deep) into `key.subkey` format.
9. Using a dict comprehension, create a mapping of numbers 1‑10 to their factorial.
10. Simulate a basic SQL "SELECT * FROM table WHERE column=value" on a list of dicts.
