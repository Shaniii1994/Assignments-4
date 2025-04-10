import random

def main():
    # Generate the secret number at random
    secret_number = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99...")

    # Get user's guess
    guess = int(input("Enter a guess: "))
    # Continue guessing until the correct number is found
    while guess != secret_number:
        if guess < secret_number:  # If guess is lower than secret number
            print("Your guess is too low")
        else:  # If guess is higher than secret number
            print("Your guess is too high")

        print()  # Print an empty line for clarity
        guess = int(input("Enter a new guess: "))  # Get a new guess

    print(f"Congrats! The number was: {secret_number}")

if __name__ == '__main__':
    main()
