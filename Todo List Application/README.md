## Todo List Application ✅

## What is this?

A beginner-friendly GUI To-Do list application built with `tkinter`. The app lets users add tasks, set optional reminders/times, and manage (add/remove/mark done) tasks in a simple interface.

## How it works

- The GUI is built with `tkinter` and provides input fields to add tasks and list widgets to display them.
- Task entries can be added and removed during runtime; reminders can be implemented by checking task times and showing notifications.
- The project demonstrates event-driven programming (button callbacks), simple state management, and basic input validation.

**Main script:** `main.py`

### Example usage

1. Open a terminal inside the `Todo List Application` folder.
2. Run: `python main.py`
3. Use the GUI to add tasks and remove or mark them as completed.

### Code snippet (conceptual)

```python
from tkinter import Tk, Listbox, Entry, Button

def add_task():
	task = entry.get()
	if task:
		listbox.insert('end', task)

root = Tk()
entry = Entry(root)
listbox = Listbox(root)
Button(root, text='Add', command=add_task).pack()
```

## Requirements

- Python 3.x (no extra packages required for the basic GUI)

## Summary

This project is an excellent starting point to learn GUI programming and can be enhanced by adding persistent storage (JSON/SQLite), better validation, reminders/notifications, or packaging as an executable.
