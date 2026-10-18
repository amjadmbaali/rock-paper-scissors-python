# Rock, Paper, Scissors (Python)

A command-line Rock–Paper–Scissors game against the computer, built as a team project for **CS360 – Programming Languages** at Yanbu Industrial College.

The project had two parts: a research study on the Python language (history, design goals, strengths and weaknesses, and where it is used), and a small program to practice Python basics such as input and output, conditions, loops and variables.

📄 **[Full project report](CS360_Report.pdf)** (Python research, code and screenshots)

## How the Game Works

- The player picks Rock, Paper or Scissors from a menu, and the computer picks randomly.
- The game decides the winner of each round.
- Every set is **3 rounds**. After each set, the total score for the player and the computer is shown.
- The player can then:
  1. Continue and keep the total score
  2. Reset the score to zero and start again
  3. Exit the game
- Invalid input is rejected and the round is repeated.

## Concepts Used

- `input()` and `print()` with string formatting
- `if / elif / else` conditions for the game rules
- Nested `while` loops for rounds and sets
- The `random` module for the computer's choice
- Variables to keep a running score across sets

## How to Run

```bash
python3 rock_paper_scissors.py
```

Requires Python 3, no external libraries.

## Example

```
Choose your move:
1) Rock
2) Paper
3) Scissors
4) Exit
Enter your choice (1-4): 1

You chose: rock
Computer chose: scissors
Result: You win!
```

## Team

Developed by Amjad Baali and a teammate as part of CS360.
