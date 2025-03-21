"""
Program: Division with Remainder
-------------------------------
This program divides two numbers and displays the quotient and remainder.
"""

def main():
    # Prompt the user to enter the dividend and divisor
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Calculate the quotient and remainder
    quotient = dividend // divisor  # Integer division (no remainder)
    remainder = dividend % divisor  # Modulo operation (remainder)

    # Display the result
    print("The result of this division is", quotient, "with a remainder of", remainder)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()