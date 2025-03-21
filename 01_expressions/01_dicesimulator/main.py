"""
Program: Dice Simulator
-----------------------
Simulate rolling two dice, three times. Prints the results of each die roll.
This program is used to show how variable scope works.
"""

# Import the random library to simulate random dice rolls
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)  # Roll the first die
    die2 = random.randint(1, NUM_SIDES)  # Roll the second die
    total = die1 + die2  # Calculate the total of the two dice
    print("Total of two dice:", total)

def main():
    die1 = 10  # A variable in the main() function
    print("die1 in main() starts as:", die1)
    
    # Simulate rolling two dice three times
    roll_dice()
    roll_dice()
    roll_dice()
    
    print("die1 in main() is:", die1)

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()