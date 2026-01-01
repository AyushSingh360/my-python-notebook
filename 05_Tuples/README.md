# Tuples

## 1. Topic definition
A tuple is an ordered, immutable collection of items.

## 2. Why tuples exist
- Provide read‑only sequences.
- Can be used as dictionary keys because they are hashable.
- Convey intent that data should not change.

## 3. Real‑world usage
- Returning multiple values from a function.
- Storing (x, y) coordinates.
- Fixed configuration sets.

## 4. Key rules & syntax
| Rule | Example | Details |
|------|---------|---------|
| Literal | `(1, "one")`   | Parentheses define a tuple. |
| Single‑element | `(42,)` | Requires a trailing comma to be a tuple. |
| Indexing | `t[0]`      | Access items by position. |
| Unpacking | `a, b = t` | Assign tuple items to multiple variables. |
| Count | `t.count(1)`   | Return number of occurrences of a value. |
| Index | `t.index("one")` | Return first index of a value. |

## 5. Immvutability & Hashability
Tuples are **immutable**—once created, they cannot be changed.
- **Security**: Ensures data (like database credentials) remains constant.
- **Hashability**: Because they are immutable, tuples containing only immutable types can be used as **dictionary keys** or added to **sets**.

![Python Mutability vs Immutability Infographic](./assets/mutability_comparison.png)
*(Placeholder: A professional technical infographic comparing Mutable and Immutable types.)*

## 6. Lists vs. Tuples: The Comparison
| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2]` | `(1, 2)` |
| Mutability | Mutable (can change) | Immutable (read-only) |
| Speed | Slower | Faster |
| Use Case | Dynamic collections | Fixed data / Constants |
| Use Case | General purpose | Data integrity / Keys |

## 7. Step‑by‑step explanation of examples
See **examples.py**.

## 8. Chapter layout
Same as other chapters.
