import random

def main():
    print("Welcome to the Guess the Number game!")
    
    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed_correctly = False

    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))  # Get input from user
        except ValueError:
            print("Please enter a valid integer.")
            continue
        
        attempts += 1
        
        if user_guess < number_to_guess:
            print("Your guess is too low.")
        elif user_guess > number_to_guess:
            print("Your guess is too high.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts!")

if __name__ == '__main__':
    main()
