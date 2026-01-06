# Exercises – Loops

Practice your loop skills with these progressively challenging exercises. Try to solve them without looking at the solutions first!

## Easy Level

### 1. Countdown Timer
Write a program that counts down from 10 to 1 using a `while` loop, then prints "Blastoff!".

**Expected Output:**
```
10
9
8
...
1
Blastoff!
```

---

### 2. Factorial Calculator
Calculate the factorial of 6 using a `for` loop. Factorial of 6 (6!) = 6 × 5 × 4 × 3 × 2 × 1 = 720.

**Hint:** Use an accumulator variable starting at 1.

---

### 3. Character Iterator
Iterate through each character in the string `"loop"` and print each character on a new line.

**Expected Output:**
```
l
o
o
p
```

---

## Medium Level

### 4. Fibonacci Sequence
Generate the first n Fibonacci numbers where n is input by the user. The Fibonacci sequence starts with 0, 1, and each subsequent number is the sum of the previous two.

**Example:** For n=7, output should be: `0 1 1 2 3 5 8`

**Hint:** Use two variables to track the last two numbers.

---

### 5. Filter Even Numbers
Given a list of numbers, create a new list containing only the even numbers using a loop (do NOT use list comprehension).

**Input:** `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
**Expected Output:** `[2, 4, 6, 8, 10]`

---

### 6. Interactive Menu System
Create an interactive menu that displays options and repeats until the user chooses option 0 to exit.

**Sample Menu:**
```
1. Start Game
2. View Scores
3. Settings
0. Exit
Choice:
```

**Hint:** Use `while True` with a `break` statement.

---

### 7. Sum of Digits
Write a program that takes a positive integer and calculates the sum of its digits using a loop.

**Example:** Input: 12345 → Output: 15 (1+2+3+4+5)

**Hint:** Use the modulo operator (%) to get the last digit, then divide by 10.

---

### 8. Multiplication Table
Create a multiplication table for a given number (1-10) using a `for` loop.

**Example for 5:**
```
5 × 1 = 5
5 × 2 = 10
...
5 × 10 = 50
```

---

## Hard Level

### 9. Number Guessing Game
Create a number guessing game where:
- The program randomly selects a number between 1 and 100
- The user has unlimited attempts to guess
- After each guess, provide "Higher" or "Lower" hints
- When correct, display "You won!" and the number of attempts

**Hint:** Import `random` module and use `random.randint(1, 100)`

---

### 10. Prime Number Generator
Generate all prime numbers less than 100 using nested loops (Sieve approach not required).

**Expected Output:** `[2, 3, 5, 7, 11, 13, ..., 97]`

**Hint:** For each number, check if it's divisible by any number from 2 to its square root. Use the `for...else` pattern.

---

### 11. List Flattening
Flatten a nested list (list of lists) into a single list using loops.

**Input:** `[[1, 2], [3, 4], [5, 6, 7]]`  
**Output:** `[1, 2, 3, 4, 5, 6, 7]`

**Hint:** Use nested loops - outer loop for sublists, inner loop for elements.

---

### 12. Greatest Common Divisor (GCD)
Implement the Euclidean algorithm using a `while` loop to find the GCD of two numbers.

**Example:** GCD(48, 18) = 6

**Algorithm:** Repeatedly replace the larger number with the remainder of dividing the larger by the smaller, until one becomes 0.

---

### 13. Pattern Printing
Print the following pyramid pattern using nested loops:

```
    *
   ***
  *****
 *******
*********
```

**Hint:** Each row has (2×row_number - 1) stars and (total_rows - row_number) leading spaces.

---

### 14. Word Frequency Counter
Given a sentence, count the frequency of each word using loops and a dictionary.

**Input:** `"the quick brown fox jumps over the lazy dog"`  
**Output:** `{"the": 2, "quick": 1, "brown": 1, ...}`

**Hint:** Use `.split()` to get words, then use a dictionary with the accumulator pattern.

---

### 15. Reverse String (No Built-in Reverse)
Reverse a string using only loops (do not use slicing `[::-1]` or `.reverse()`).

**Input:** `"Python"`  
**Output:** `"nohtyP"`

**Hint:** Build a new string by iterating backwards through indices.

---

## Bonus Challenges

### 16. Find All Pairs with Target Sum
Given a list of numbers and a target sum, find all pairs of numbers that add up to the target.

**Input:** `numbers = [2, 7, 11, 15, 3]`, `target = 9`  
**Output:** `[(2, 7)]`

---

### 17. Pascal's Triangle
Generate the first n rows of Pascal's Triangle using nested loops.

**Example for n=5:**
```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

---

### 18. Collatz Sequence
For a given positive integer n, generate the Collatz sequence until it reaches 1:
- If n is even: n = n / 2
- If n is odd: n = 3n + 1

**Example for n=6:** `6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1`

Count how many steps it takes to reach 1.

---

## Test Your Knowledge

After completing the exercises, you should be comfortable with:
- ✅ Using `for` and `while` loops appropriately
- ✅ Understanding `break`, `continue`, and `else` clauses
- ✅ Working with `range()`, `enumerate()`, and `zip()`
- ✅ Implementing nested loops for multi-dimensional problems
- ✅ Using accumulator and search patterns
- ✅ Avoiding infinite loops

**See `solutions.py` for complete solutions with explanations!**
