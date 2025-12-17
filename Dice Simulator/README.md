
# Dice Simulator 🎲

## What is this?
A basic dice simulator demonstrating random number generation and interactive user prompts to roll one or more dice repeatedly. It’s a concise learning project to practice Python’s `random` module and simple I/O.

## How it works
- The script prompts the user for the number of dice and rolls, then uses `random.randint(1, 6)` to simulate each die roll.
- Results are displayed after each roll and optionally summarized by counts or totals.

**Main script:** `Dice_Simulator.py`

### Example snippet
```python
import random

def roll_die():
	return random.randint(1, 6)

print('Rolling 2 dice...')
print(roll_die(), roll_die())
```

### Requirements
- Python 3.x (no external packages required)

### How to run
1. Run: `python Dice_Simulator.py`
2. Enter the number of dice and follow prompts to roll or quit.

## Summary
Small, interactive program ideal for beginners to learn randomness, loops, and basic user interaction. Suggested enhancements: add custom die sizes, roll statistics, or a GUI wrapper.

