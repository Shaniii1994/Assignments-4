MINIMUM_HEIGHT = 50  # Minimum height required to ride (in arbitrary units)

def main():
    while True:
        height = input("How tall are you? ")  # Ask the user for their height
        
        if height == "":  # If the user presses Enter without entering anything, stop the program
            break

        height = float(height)  # Convert input to a float
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
