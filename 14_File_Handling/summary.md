# Summary – File Handling

## File Modes Cheat Sheet

| Mode | Name | Description | Pointer | Existing File | Missing File |
|---|---|---|---|---|---|
| `'r'` | Read | Default. Read-only. | Start | Opens | Error |
| `'w'` | Write | Writing. **Truncates** (Wipes)! | Start | Overwrites | Creates |
| `'a'` | Append | Writing. Adds to end. | End | Appends | Creates |
| `'x'` | Create | Safe create. | Start | Error | Creates |
| `'r+'`| Update | Read and Write. | Start | Opens | Error |

**Modifiers:**
- `'b'`: Binary mode (e.g., `'rb'`, `'wb'`). For images, audio.
- `'t'`: Text mode (Default). Handles encoding.

## Essential Syntax

### Result-Guaranteed Open (Context Manager)
**ALWAYS** use this pattern to prevent memory leaks.
```python
with open("filename.txt", "mode", encoding="utf-8") as f:
    # Do work
# Files closes automatically here
```

### Reading Methods

- `f.read()`: Everything as one string.
- `f.readline()`: One line at a time.
- `f.readlines()`: List of all lines `['a\n', 'b\n']`.
- `for line in f:`: **Best/Most Efficient way**.

### File Pointer

- `f.tell()`: Where am I? (Byte index)
- `f.seek(offset, from_where)`: Teleport.
    - `0`: Start
    - `2`: End

## Modern Paths (`pathlib`)

```python
from pathlib import Path

p = Path("data") / "file.txt" # Cross-platform joining
if p.exists():
    t = p.read_text()
    p.write_text("New content")
```

## Structured Data

### JSON
```python
import json
json.dump(obj, f)  # Write
data = json.load(f) # Read
```

### CSV
```python
import csv
writer = csv.writer(f)
writer.writerow(['A', 'B'])
```

## Best Practices Checklist

✅ Always use `with open(...)`.  
✅ Always verify `encoding="utf-8"` for text files.  
✅ Use `pathlib` for paths instead of string concatenation.  
✅ Use `w` mode carefully (it deletes data!).  
✅ Handle `FileNotFoundError`.  
