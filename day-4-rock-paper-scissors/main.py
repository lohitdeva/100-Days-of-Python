# This script will replicate the classic kids game - Rock, Paper, Scissors.
# Fun Addition - We will use ASCII art to denote user and computer choice.
# Created by: Lohit Deva
# 08/12/2022

# rpsart stands for Rock, Paper, Scissors art. It is a custom module created
# and contains only the ASCII art for rock, paper, and scissors that will be used in
# this script
import rpsart
import random

options = [rpsart.rock, rpsart.paper, rpsart.scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
computer_choice = random.randint(0,2)

# Checking if user picked a valid option
if user_choice >= 0 and user_choice <= 2:
	
	print("\nYou chose:\n")
	print(options[user_choice])

	print("\nComputer chose:\n")
	print(options[computer_choice])

	# In case of a tie
	if user_choice == computer_choice:
		print("\nIt's a tie!\n")

	# If there is no tie
	else:

		# If the user has picked rock
		if user_choice == 0:

			# Paper beats rock, user loses
			if computer_choice == 1:
				print("\nYou lose!\n")

			# Rock beats scissors, user wins
			else:
				print("\nYou win!\n")

		# If the user has picked paper
		elif user_choice == 1:

			# Paper beats rock, user wins
			if computer_choice == 0:
				print("\nYou win!\n")

			# Scissors beat paper, user loses
			else:
				print("\nYou lose!\n")

		# If the user has picked scissors
		else:		

			# Rock beats scissors, user loses
			if computer_choice == 0:
				print("\nYou lose!\n")

			# Scissors beat paper, user wins
			else:
				print("\nYou win!")

# User picked an invalid option
else:
	print("\nYou picked an invalid option. You lose!\n")
