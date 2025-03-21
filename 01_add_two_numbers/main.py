"""
Program: add2numbers
--------------------
This program asks the user for two integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")
    
    # Prompt the user to enter the first number and convert it to an integer
    num1 = int(input("Enter first number: "))
    
    # Prompt the user to enter the second number and convert it to an integer
    num2 = int(input("Enter second number: "))
    
    # Calculate the sum of the two numbers
    total = num1 + num2
    
    # Print the total sum with an appropriate message
    print("The total is", total)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()