def main():
    curr_value = int(input("Enter a number: "))  # Get the initial number from the user
    while curr_value < 100:
        print(curr_value, end=" ")  # Print the current value
        curr_value = curr_value * 2  # Double the value

if __name__ == '__main__':
    main()
