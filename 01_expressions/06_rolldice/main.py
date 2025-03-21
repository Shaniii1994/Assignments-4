"""
Program: Dice Roll Simulator
---------------------------
This program simulates rolling two dice and prints the results of each roll as well as the total.
"""

# Import the random library to simulate random dice rolls
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    # Optional: Set a seed for debugging (uncomment the line below to use it)
    # random.seed(1)
    
    # Roll the first die
    die1 = random.randint(1, NUM_SIDES)
    
    # Roll the second die
    die2 = random.randint(1, NUM_SIDES)
    
    # Calculate the total of the two dice
    total = die1 + die2
    
    # Print the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()