def main():
    print("Welcome to Mad Libs!")
    # Collecting user inputs
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective1 = input("Enter an adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb: ")
    adjective2 = input("Enter another adjective: ")
    
    # Story template
    story = f"Once upon a time, there was a {adjective1} {noun1} who loved to {verb1}. " \
            f"One day, it found a {adjective2} {noun2} and decided to {verb2} with it. " \
            "They had a lot of fun and lived happily ever after."

    # Display the completed story
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == '__main__':
    main()
