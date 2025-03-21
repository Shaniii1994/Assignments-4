"""
Program: Sum of Numbers in a List
---------------------------------
This program calculates the sum of numbers in a list using a function.
"""

def add_many_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far = 0  # Initialize the total sum to 0
    for number in numbers:
        total_so_far += number  # Add each number to the total sum
    return total_so_far  # Return the final sum

def main():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]
    
    # Calculate the sum of the numbers using the function
    sum_of_numbers = add_many_numbers(numbers)
    
    # Print the sum of the numbers
    print(sum_of_numbers)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()