# Creating Table 🧾

## What is this?
A small utility that shows how to build and print formatted tables in the console using either `prettytable` or Python string formatting.

**Main script:** `Create_Table.py`

### Example (PrettyTable)
```python
from prettytable import PrettyTable

t = PrettyTable(['Name', 'Score'])
t.add_row(['Alice', 90])
t.add_row(['Bob', 82])
print(t)
```

### How to run
1. (Optional) Install PrettyTable: `pip install prettytable`
2. Run: `python Create_Table.py`

## Summary
Useful for presenting tabular output in CLI applications and for small reporting tasks.

