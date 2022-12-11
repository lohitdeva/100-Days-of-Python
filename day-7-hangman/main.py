# This script recreates the classic game, Hangman.
# Users have six lives and can guess characters of a hidden word to eventually reveal the word.
#
# The ASCII art and word list for this project are included in separate files to make the code more readable.

# Created by: Lohit Deva
# 10/12/2022

import random
import hangman_art as art
import hangman_words as words

print("\n", art.logo, "\n", sep='')

# Picks a random word form the word list
chosen_word = random.choice(words.word_list)

result = list()

# Creates an array of blanks where the blanks will be substituted with each correct guess over the course of the game
for i in range(len(chosen_word)):
	result.append('_')

# Prints out the result array in the form of a string.
# The join() function is used to concatenate list elements together into a string and the string specified before
# the function acts as a separator.
print(f'\n{" ".join(result)}\n')

# Here we initialize the number of lives and the game end condition. We also keep track of the guesses that the user
# has already made.
game_end = False
lives = 6
guesses = ''

# Begin game
while not game_end:
	guess = input("\nGuess a letter\n").lower()

	# Checks if the user has already guessed a certain letter. If they have an error message is displayed and they
	# are not penalized.
	if guess in guesses:
		print(f"\nYou already guessed '{guess}', try again!\n")
		continue
	
	# If the user has not guessed a letter before, it is added to the guesses string, where it will be compared with
	# during the next run of the loop.
	else:
		guesses += guess
    
	# Checks if the guessed letter is not in the randomly selected word and reduces a life to penalize the user.
	if guess not in chosen_word:
		print("\nWrong guess!\n")
		lives -= 1
	
	# If the guessed letter is in the word, then the letter is added to its position in the results array.
	else:
		print("\nRight guess!\n")
		for i in range(len(chosen_word)):
			if guess == chosen_word[i]:
				result[i] = guess
    	
	# Here the number of lives and the results array is printed out in the form of a string to keep the user informed
	# about their progress.
	print(f'{" ".join(result)}')
	print(art.stages[lives])

	# This validation checks if the game has to be ended, either due to the word being guessed or if there
	# are no more lives remaining
	if '_' not in result or lives == 0:
		game_end = True

# If the word has been fully guessed, the user wins.
if '_' not in result:
	print("\nYou win!\n")

# If the user has lost all their lives, they lose and the correct answer is revealed.
else:
	print("\nYou lose!\n")
	print(f'The word was {chosen_word}\n')
