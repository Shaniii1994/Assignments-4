import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    characters = string.ascii_lowercase  # Always include lowercase letters

    # Add the selected character types to the pool of characters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Ensure the password is at least as long as the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    
    # Get user input for password criteria
    try:
        length = int(input("Enter the desired password length: "))
        if length < 8:
            print("Password length should be at least 8 characters for better security.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    
    # Show the generated password
    print(f"\nYour secure password is: {password}")

if __name__ == "__main__":
    main()
