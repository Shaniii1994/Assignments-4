"""
Program: Hypotenuse Calculator
-------------------------------
This program calculates the length of the hypotenuse of a right triangle
using the Pythagorean theorem.
"""

import math  # Import the math library to use the sqrt function

def main():
    # Prompt the user to enter the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    # Display the length of the hypotenuse
    print("The length of BC (the hypotenuse) is:", bc)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()