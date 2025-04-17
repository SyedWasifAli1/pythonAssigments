"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.
Prints the results of each die roll.
This program is used to show how variable scope works.
"""

# Import random to simulate dice rolls
import random

# Define how many sides each die has
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    Variables die1 and die2 are local to this function.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Rolled: {die1} + {die2} = {total}")

def main():
    # Variable die1 in this function is different from die1 in roll_dice()
    die1 = 10
    print("die1 in main() starts as:", die1)

    # Roll the dice 3 times
    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() ends as:", die1)

# Standard Python entry point
if __name__ == '__main__':
    main()
