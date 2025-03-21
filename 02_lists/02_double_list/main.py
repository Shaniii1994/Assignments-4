"""
Program: Double Elements in a List
----------------------------------
This program doubles each element in a list of numbers.
"""

def main():
    # Create a list of numbers
    numbers = [1, 2, 3, 4]

    # Loop through the indices of the list
    for i in range(len(numbers)):
        # Double the element at index i
        numbers[i] = numbers[i] * 2

    # Print the updated list
    print(numbers)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()