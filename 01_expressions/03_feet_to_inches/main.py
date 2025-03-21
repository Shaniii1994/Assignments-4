"""
Program: Feet to Inches Converter
---------------------------------
This program converts a measurement in feet to inches.
"""

# Conversion factor: There are 12 inches in 1 foot
INCHES_IN_FOOT = 12

def main():
    # Prompt the user to enter the number of feet
    feet = float(input("Enter number of feet: "))
    
    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT
    
    # Display the result
    print("That is", inches, "inches!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()