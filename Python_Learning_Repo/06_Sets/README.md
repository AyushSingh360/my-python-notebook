# Sets

## 1. Topic definition
A set is an unordered collection of **unique** hashable items.

## 2. Why sets exist
- Fast membership testing (`O(1)` average).
- Automatic duplicate removal.
- Useful for mathematical operations (union, intersection, difference).

## 3. Real‑world usage
- Removing duplicate entries from a list of emails.
- Checking if a user ID already exists.
- Performing tag‑based searches.

## 4. Key rules & syntax
| Rule | Example |
|------|---------|
| Literal | `{1, 2, 3}` |
| Empty set | `set()` |
| Add element | `s.add(4)` |
| Remove element | `s.discard(2)` |
| Union | `s1 | s2` |
| Intersection | `s1 & s2` |
| Difference | `s1 - s2` |
| Membership | `x in s` |
| Set comprehension | `{x*x for x in range(5)}` |

## 5. Step‑by‑step explanation of examples
See **examples.py**.

## 6. Chapter layout
Same as other chapters.
