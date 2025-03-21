"""
Program: Triangle Perimeter Calculator
--------------------------------------
This program calculates the perimeter of a triangle based on the lengths of its sides.
"""

def main():
    # Prompt the user to enter the lengths of the three sides of the triangle
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter of the triangle
    perimeter = side1 + side2 + side3

    # Print the perimeter of the triangle
    print("The perimeter of the triangle is", perimeter)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()