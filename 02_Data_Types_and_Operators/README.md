# Data Types & Operators

## 1. Topic definition
Data types describe the kind of value a variable holds (int, float, str, bool, etc.). Operators manipulate those values.

## 2. Why they exist
- Provide a predictable way to store, retrieve, and compute data.
- Enable mathematical, logical, and collection operations.

## 3. Real‑world usage
- Numerical calculations (Finance, Physics, AI)
- Text processing (Logs, Data cleaning)
- Control flow (Feature flags, None-checks)

## 4. Technical Deep-Dive: Individual Data Types

### 4.1. Integers (`int`)
Python integers have **arbitrary precision**, meaning they are bounded only by the available memory. This is achieved through a "bignum" implementation where large numbers are stored in an array of digits.

![Technical Overview: Python Integer Memory & Precision](./assets/integer_tech.png)

- **Memory**: Standard 64-bit integers are small objects, but large integers grow dynamically.
- **Operations**: Fast for common sizes, but performance degrades for astronomically large numbers.

### 4.2. Floating-Point Numbers (`float`)
Python floats are implemented using binary floating-point arithmetic following the **IEEE 754** double-precision standard (64-bit).

![Technical Overview: IEEE 754 Floating Point Format](./assets/float_tech.png)

- **Structure**: 1 sign bit, 11 exponent bits, and 52 mantissa/fraction bits.
- **Precision**: Approximately 15-17 significant decimal digits. Note that binary floats can represent some decimal fractions (like 0.1) only approximately.

### 4.2.1. Complex Numbers (`complex`)
Python has built-in support for complex numbers in the format `a + bj`, where `j` represents the imaginary unit ($\sqrt{-1}$).

```mermaid
graph LR
    C["Complex(3, 4)"] --> R["Real Part: 3.0"]
    C --> I["Imaginary Part: 4.0j"]
    style C fill:#e1f5fe,stroke:#01579b
```
- **Usage**: High-level scientific computing and electrical engineering.

### 4.3. Booleans (`bool`)
The `bool` type is a subclass of `int`. There are only two instances: `True` (effectively `1`) and `False` (effectively `0`).

![Technical Overview: Boolean Logic & Under-the-hood Integer Mapping](./assets/boolean_tech.png)

- **Logic**: Used in control structures (if/while) and logical expressions (`and`, `or`, `not`).

### 4.4. Dictionaries (`dict`)
Dictionaries are the most optimized collection in Python, implemented as a **Highly Tuned Hash Table**.

![Technical Overview: Python Dictionary Hash Table Mechanics](./assets/dictionary_tech.png)

- **Complexity**: Average O(1) for lookups, insertions, and deletions.
- **Keys**: Must be hashable (immutable) to ensure consistent index calculation.

### 4.5. Sets (`set`)
A set is an unordered collection of unique, hashable items. Under the hood, it uses a hash table similar to a dictionary but without values.

![Technical Overview: Set Mechanics & Set Operations](./assets/set_tech.png)

- **Uniqueness**: Automatically discards duplicate entries.
- **Operations**: Highly efficient for mathematical operations like Union (`|`), Intersection (`&`), and Difference (`-`).

### 4.6. The Null Type (`NoneType`)
`None` is a special constant in Python used to represent the absence of a value or a null pointer. It is the sole instance of the `NoneType` class.

```mermaid
graph TD
    Var["Variable"] -- "Points to" --> N["Single Object: None"]
    subgraph "NoneType Singleton"
    N
    end
    style N fill:#eceff1,stroke:#455a64,stroke-dasharray: 5 5
```
- **Usage**: Default return value for functions, optional parameters, and state initialization.

### 4.7. Binary Data (`bytes`)
`bytes` objects are immutable sequences of single bytes (integers in the range 0-255).

```mermaid
graph LR
    B["b'Hello'"] --> H["[72, 101, 108, 108, 111]"]
    style B fill:#eceff1,stroke:#607d8b
```
- **Usage**: Handling raw binary data, network communication, and file I/O.

### 4.8. Ranges (`range`)
The `range` type represents an immutable sequence of numbers and is commonly used for looping a specific number of times in for-loops.

```mermaid
graph LR
    R["range(0, 10, 2)"] --> S["[0, 2, 4, 6, 8]"]
    style R fill:#fff9c4,stroke:#fbc02d
```
- **Memory**: Extremely memory-efficient as it always takes the same small amount of memory, no matter the size of the range it represents (it only stores start, stop, and step).

## 5. Operator Precedence
When multiple operators are used in one expression, Python follows a specific order of execution (PEMDAS/BODMAS).

![Python Operator Precedence Guide](./assets/operator_precedence.png)

| Precedence | Operator | Description |
|------------|----------|-------------|
| 1 (Highest) | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `* / // %` | Multiplication, Division, etc. |
| 4 | `+ -` | Addition, Subtraction |
| 5 | `== != > <` | Comparison Operators |
| 6 | `not and or` | Logical Operators |

## 5. Step‑by‑step explanation of examples
See **examples.py** for practical demonstrations.

## 6. Chapter layout
Same as other chapters.
