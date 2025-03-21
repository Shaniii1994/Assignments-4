"""
Program: Age Riddle Solver
--------------------------
This program calculates the ages of Anton, Beth, Chen, Drew, and Ethan based on the given relationships.
"""

def main():
    # Anton's age is given as 21 years old
    anton = 21
    
    # Beth is 6 years older than Anton
    beth = 6 + anton
    
    # Chen is 20 years older than Beth
    chen = 20 + beth
    
    # Drew is as old as Chen's age plus Anton's age
    drew = chen + anton
    
    # Ethan is the same age as Chen
    ethan = chen
    
    # Print out all of the ages!
    print("Anton is", anton)
    print("Beth is", beth)
    print("Chen is", chen)
    print("Drew is", drew)
    print("Ethan is", ethan)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()