from art import logo
import random

def checkNumber():
    '''This function allows users to keep trying to guess the secret number
    as long as they have lives left. It also displays whether their guess was higher or lower
    than the secret number, and how many lives they have left.'''
    
    # Accessing the lives variable from the global scope that holds the number of lives
    # the user has left
    global lives
    
    # Game loop - runs as long as user has lives left. 
    while lives > 0:
        guess = int(input("\nGuess a number:\n"))
        
        if guess != number:
            lives -= 1
            if guess > number:
                print("\nThat was too high, try guessing lower. 🔽")
            else:
                print("\nThat was too low, try guessing higher. 🔼")
            print(f"You have {lives} lives remaining")
        else:
            # Returns to main function once the correct number is guessed.
            return
        
    else:
        # Returns to main function once the number of lives are exhausted
        return    
        
print(logo)
print("I'm thinking of a number between 1 and 100, can you guess what it is?")

_ = input("Choose a difficulty. Type 'easy' or 'hard'\n").strip().lower()
while _ != 'easy' and _ != 'hard':
    _ = input("That was not a valid option, try again\n").strip().lower()

if _ == 'easy':
    lives = 10
else:
    lives = 5

# In the f-string, the first letter of the difficulty is capitalized and then concatenated to the remaining substring
print(f"\nYou have chosen '{_[0].upper() + _[1: ]}' difficulty. You get {lives} lives")

number = random.randint(1, 100)

checkNumber()

if lives > 0:
    print("\nGood job! You guessed correctly 🎉")
else:
    print("\nOh no, you ran out of lives! You lost. 😭")