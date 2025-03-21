"""
Program: Mad Libs Generator
---------------------------
This program prompts the user for an adjective, a noun, and a verb,
and then prints a fun sentence using those words.
"""

# Constant for the beginning of the sentence
SENTENCE_START = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    # Prompt the user for an adjective, noun, and verb
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")

    # Combine the inputs with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()