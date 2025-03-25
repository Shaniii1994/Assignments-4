def main():
    lst = []  # Create an empty list to store the values

    val = input("Enter a value: ")  # Prompt the user for the first input
    while val:  # While the user doesn't press enter without typing anything
        lst.append(val)  # Add the entered value to the list
        val = input("Enter a value: ")  # Prompt for the next input

    print("Here's the list:", lst)  # Print the final list when the loop ends

if __name__ == '__main__':
    main()
