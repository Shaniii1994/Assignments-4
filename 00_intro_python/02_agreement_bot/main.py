"""
Program: Favorite Animal
------------------------
This program asks the user for their favorite animal and responds with a message.
"""

def main():
    # Prompt the user to enter their favorite animal
    animal = input("What's your favorite animal? ")
    
    # Respond with a message including the user's favorite animal
    print("My favorite animal is also", animal + "!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()