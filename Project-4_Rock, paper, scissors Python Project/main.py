import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "You lose!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "You lose!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "You lose!"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'quit' to stop playing): ").lower()
        
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

if __name__ == '__main__':
    main()
