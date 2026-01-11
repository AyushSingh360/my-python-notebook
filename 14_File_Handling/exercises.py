# Exercises – File Handling

import os

## Easy Level

### 1. Basic Write
Write a script that creates a file named `my_info.txt` and writes your name and age on separate lines using the `with` statement.

### 2. Basic Read
Read the `my_info.txt` file you just created and print its content line by line.

### 3. Append Mode
Open `my_info.txt` in append mode and add "I love Python!" as a new line. Verify the change by reading it again.

### 4. Line Counting
Create a file `poem.txt` with at least 5 lines of text. Write a script to count how many lines are in the file.

### 5. List to File
Given a list `colors = ["Red", "Green", "Blue"]`, write each color to a new file `colors.txt`, ensuring each is on a new line.

## Medium Level

### 6. Copy File
Write a function `copy_file(source, destination)` that reads content from source and writes it to destination.

### 7. File Statistics
Write a script that reads a text file and prints:
- Total characters
- Total words
- Total lines

### 8. Find and Replace
Write a script that reads a file, replaces all occurrences of the word "bad" with "good", and saves it to a NEW file.

### 9. Safe Open
Write a function `read_safe(filename)` that attempts to open a file. If it doesn't exist, print "File not found" instead of crashing.

### 10. CSV Writer
Use the `csv` module to create `students.csv`. Write a header "Name,Grade" and add 3 rows of data.

### 11. Log Parser
Create a `server.log` with lines like "INFO: Started", "ERROR: Crash", "INFO: Running". Write a script to extract only the lines starting with "ERROR".

## Hard Level

### 12. Binary Copy (Image)
Write a script to copy an image file (e.g., `image.png`) to `image_copy.png`. *Hint: Use mode 'rb' and 'wb'.*

### 13. JSON Config Store
Create a dictionary representing game settings (volume, difficulty). Save it to `settings.json`. Then, load it back and print the "volume".

### 14. File Walker
Use `os.walk()` (or `pathlib`) to list ALL files in the current directory and its subdirectories.

### 15. Large File Chunk Reader
Write a generator function that reads a file in chunks of 1024 bytes (not lines). Use it to read a hypothetical large file.

### 16. Context Manager Class
Create a class `LogWriter` that opens a file in `__enter__` and writes "Start Logging" and in `__exit__` writes "End Logging" and closes it.

### 17. Multi-File Search
Write a function that takes a word and a list of filenames. It should search the word in all files and print the filename and line number where found.

### 18. File Seek/Tell Reverse
Write a script that reads the LAST 10 characters of a file without reading the whole file. *Hint: seek relative to end.*

## Bonus Challenges

### 19. CSV to JSON Converter
Write a script that converts a CSV file into a JSON file (list of dictionaries).

### 20. Atomic Write
Write a function `write_atomic(filename, content)` that writes to a temporary file first, then renames it to the target filename (safer against crashes).

### 21. Directory Cleaner
Write a script that looks into a folder and deletes all `.tmp` files. *Be careful!*

**See `solutions.py` for complete solutions!**
