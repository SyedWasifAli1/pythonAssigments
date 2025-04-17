import random  # Random module import for generating random numbers

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
    # Roll first die (random number between 1 and NUM_SIDES)
    die1: int = random.randint(1, NUM_SIDES)
    # Roll second die (random number between 1 and NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Calculate the total sum of both dice
    total: int = die1 + die2
    
    # Print the result
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


# This line is required to call the main function when the program runs
if __name__ == '__main__':
    main()
