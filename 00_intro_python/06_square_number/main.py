"""
Program: Square Calculator
--------------------------
This program calculates the square of a number entered by the user.
"""

def main():
    # Prompt the user to enter a number
    num = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = num ** 2
    
    # Print the result
    print(f"{num} squared is {square}")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()