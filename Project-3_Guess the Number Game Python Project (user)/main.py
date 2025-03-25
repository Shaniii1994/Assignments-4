def main():
    print("Welcome to the Guess the Number game!")
    
    # Ask the user to think of a number between 1 and 100
    print("Please think of a number between 1 and 100 and keep it in your mind.")
    print("I will try to guess it!")

    low = 1
    high = 100
    guesses = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        # The computer guesses the middle number
        guess = (low + high) // 2
        guesses += 1
        
        print(f"My guess is: {guess}")
        
        # Ask the user for feedback
        feedback = input("Is my guess too high, too low, or correct? (high/low/correct): ").lower()

        if feedback == "high":
            high = guess - 1
        elif feedback == "low":
            low = guess + 1
        elif feedback == "correct":
            guessed_correctly = True
            print(f"Yay! I guessed your number {guess} in {guesses} attempts.")
        else:
            print("Please enter a valid response (high/low/correct).")

if __name__ == '__main__':
    main()
