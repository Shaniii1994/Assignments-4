import random

# List of words for the game
words = ["python", "java", "hangman", "computer", "programming", "developer", "challenge"]

def get_random_word():
    """Return a random word from the list."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with guessed letters and underscores for missing letters."""
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    print("Welcome to Hangman!")
    
    # Get a random word from the list
    word = get_random_word()
    guessed_letters = []  # Keep track of guessed letters
    attempts = 6  # Number of attempts allowed
    guessed_word = "_" * len(word)  # Display word with underscores

    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guesses left: {attempts}")
        
        # Take user input
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! {guess} is in the word.")
        else:
            print(f"Oops! {guess} is not in the word.")
            attempts -= 1
        
        # Check if the user has guessed the whole word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")

if __name__ == "__main__":
    hangman()
