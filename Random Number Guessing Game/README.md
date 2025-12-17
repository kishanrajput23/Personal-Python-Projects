# Random Number Guessing Game 🎯

## What is this?
A simple command-line game where the program picks a random number and the player tries to guess it within a limited number of attempts. The game teaches basic input handling, loops, conditionals and using Python’s `random` module.

## How it works
- The program selects a random integer (commonly from 1 to 100).
- The player inputs guesses and the program responds whether the guess is too low, too high, or correct.
- The player keeps guessing until they find the number or run out of attempts; the final score or number of attempts is shown.

**Main script:** `random_no_guessing_game.py`

### Example code snippet
```python
import random

answer = random.randint(1, 100)
tries = 0
while True:
	guess = int(input('Enter your guess (1-100): '))
	tries += 1
	if guess == answer:
		print(f'Correct! You guessed in {tries} tries.')
		break
	elif guess < answer:
		print('Too low, try again.')
	else:
		print('Too high, try again.')
```

### How to run
1. Run: `python random_no_guessing_game.py`
2. Enter guesses when prompted.

## Summary
Friendly beginner project that reinforces control flow and randomness concepts. Try adding difficulty levels, attempt limits, or a high-score tracker as enhancements.

