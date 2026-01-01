# Lists

## 1. Topic definition
A list is an ordered, mutable collection of items.

## 2. Why lists exist
- Store sequences of data (users, scores, filenames).
- Flexible sizing (grow/shrink dynamically).

## 3. Real‑world usage
- A shopping cart.
- Rows from a spreadsheet.
- A playlist of songs.

## 4. Key rules & syntax
| Rule | Example | Details |
|------|---------|---------|
| Literal | `[1, 2, 3]` | Square brackets define a list. |
| Indexing | `L[0]`, `L[-1]` | Access items by position (0-based). |
| Slicing | `L[1:3]` | Extract a sub-list (start:end). |
| `append(x)` | `L.append(4)` | Adds an item to the end. |
| `extend(iterable)` | `L.extend([5, 6])` | Appends items from another list. |
| `insert(i, x)` | `L.insert(0, 0)` | Inserts an item at a specific index. |
| `pop(i)` | `L.pop()` | Removes and returns the last item (or at index `i`). |
| `remove(x)` | `L.remove(1)` | Removes the first occurrence of `x`. |
| `sort()` | `L.sort()` | Sorts the list in-place. |
| `reverse()` | `L.reverse()` | Reverses the list in-place. |
| `clear()` | `L.clear()` | Removes all items from the list. |

```mermaid
graph LR
    subgraph "Common List Methods"
    A["append(x)"] --> B["Add to end"]
    C["insert(i, x)"] --> D["Insert at index"]
    E["pop()"] --> F["Remove & return last"]
    G["remove(x)"] --> H["Remove first occurrence"]
    I["extend(list)"] --> J["Concatenate list"]
    end
    style A fill:#e3f2fd,stroke:#1e88e5,color:#000
    style C fill:#e3f2fd,stroke:#1e88e5,color:#000
    style E fill:#fce4ec,stroke:#d81b60,color:#000
    style G fill:#fce4ec,stroke:#d81b60,color:#000
    style I fill:#e8f5e9,stroke:#43a047,color:#000
```

![Python List Memory Structure (Dynamic Array)](./assets/list_memory_structure.png)

## 5. Memory Management (Dynamic Arrays)
Python lists are implemented as **dynamic arrays**. This provides high performance for common operations:
- **Over-allocation**: Python allocates more memory than strictly needed to accommodate future growth.
- **Resizing**: When the allocated space is exhausted, Python automatically allocates a larger block and migrates items.
- **Performance**: This architecture ensures that `append` operations have an **Amortized O(1)** time complexity.

## 6. Slicing Deep Dive
Slicing allows you to get parts of a list using `list[start:stop:step]`.
- `L[:2]` - from the beginning to index 2 (exclusive).
- `L[1:]` - from index 1 to the end.
- `L[::2]` - every second item (step size 2).
- `L[::-1]` - reverse the list.

```mermaid
graph TD
    subgraph "Python Indexing & Slicing"
    direction LR
    List["['P', 'y', 't', 'h', 'o', 'n']"]
    
    subgraph Positive_Indices
    PIM["0  1  2  3  4  5"]
    end
    
    subgraph Negative_Indices
    NIM["-6 -5 -4 -3 -2 -1"]
    end
    
    List --- PIM
    List --- NIM
    
    Slicing["L[start:stop:step]"] -.-> Ex["L[1:4] → ['y', 't', 'h']"]
    end
    style List fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    style Slicing fill:#fff9c4,stroke:#fbc02d,color:#000
    style Ex fill:#e8f5e9,stroke:#2e7d32,color:#000
```

## 7. Step‑by‑step explanation of examples
See **examples.py**.

## 8. Chapter layout
Standard layout.
