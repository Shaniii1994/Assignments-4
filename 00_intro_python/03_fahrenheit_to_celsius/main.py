"""
Program: Fahrenheit to Celsius Converter
----------------------------------------
This program converts a temperature from Fahrenheit to Celsius.
"""

def main():
    # Prompt the user to enter a temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert the temperature to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Print the result with both Fahrenheit and Celsius values
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()