(The file `c:\Users\KISHAN\Downloads\temp\Personal-Python-Projects\Tic-Tac-Toe-Game\README.md` exists, but contains only whitespace)
# Tic-Tac-Toe Game ❌⭕

## What is this?
A simple implementation of the classic Tic-Tac-Toe game playable in the console. It demonstrates board representation, win/draw detection, and player input handling.

## How it works
- The board is represented as a 3x3 grid (list of lists or flat list).
- Two players alternate entering moves (X and O) by specifying a row/column or cell index.
- After each move, the program checks for a winning line (three identical marks in a row/column/diagonal) or a draw.

**Main script:** `Tic-Tac-Toe-Game.py`

### Example snippet
```python
# Represent board and check wins
board = [' '] * 9
def check_win(b, mark):
	wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
	return any(b[a]==b[b_]==b[c]==mark for a,b_,c in wins)
```

### How to run
1. Run: `python Tic-Tac-Toe-Game.py`
2. Follow on-screen prompts to enter moves (e.g., cell number or row/col).

## Summary
Great beginner project to practice control flow, data structures, and game logic. Consider adding a single-player mode with a simple AI (minimax or heuristic) as an enhancement.

