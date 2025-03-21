"""
Program: Seconds in a Year Calculator
------------------------------------
This program calculates the number of seconds in a year using constants.
"""

# Constants for the calculation
DAYS_PER_YEAR = 365  # Number of days in a year
HOURS_PER_DAY = 24   # Number of hours in a day
MIN_PER_HOUR = 60    # Number of minutes in an hour
SEC_PER_MIN = 60     # Number of seconds in a minute

def main():
    # Calculate the number of seconds in a year
    seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the result in a nice message
    print("There are", seconds_in_year, "seconds in a year!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()