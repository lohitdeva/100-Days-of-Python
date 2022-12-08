print('''\n\n*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************\n\n\n''')

print("Welcome to the Treasure Island. Your purpose is to find the hidden treasure and fulfill your destiny")
print("But beware of the dangers that lie ahead of you...")

# Beginning of the journey. Going left continues the journey whereas going right ends it.
# input() directly used inside if to avoid using an additional variable
if(input("\nYou begin your adventure at a crossroad. Type \"left\" to go left or \"right\" to go right. ").lower() == 'left'):
	print("\nYou turned left...")
	print("An enormous lake lies ahead of you, stretching all the way to the horizon.")
	print("You can either swim across the lake or try waiting.")
	
	# Second branch of the journey. Swimming causes death while waiting causes a boat to spawn to continue journey.
	# Again, using a variable to store the choice is avoided.
	if(input("\nType \"swim\" to begin swimming across the river or \"wait\" to wait and see and what happens. ").lower() == 'wait'):
		print("\nYou waited...")
		print("A boat appears over the horizon, heading towards you.")
		print("The boat has nobody on board, and automatically begins to set sail once you board.")
		print("You arrive at a small island, and there are three doors (red, yellow, and blue) in front of you.\nThe treasure lies behind one of these three doors. Which one do you pick?")
		
		# Here a variable is used to store the choice as there are multiple options to consider.
		# Also, in this case the variable is used to denote user choice in the form of an f-string.
		door_choice = input("\nType \"red\" to open the red door, \"yellow\" to open the yellow door, or \"blue\" to open the blue door. ").lower()
		
		# The purpose of this if condition is to denote that a choice has been selected from among the options presented to the user.
		if door_choice == 'red' or door_choice == 'blue' or door_choice == 'yellow':
			print(f"\nYou open the {door_choice} door...")
			
			# This is the final step of the journey. Opening the yellow door wins you the treasure whereas the other doors lead to death.
			if door_choice == 'red':
				print("A giant wall of flames erupts from the door and engulfs you, burning you to a crisp")
			elif door_choice == 'blue':
				print("A horde of wild beasts emerge from the door, trampling you to death")
			else:
				print("You found the hidden the secret hidden treasure and can now live happily ever after.")
		# If none of the provided door options are chosen
		else:
			print("\nYou try walking around the doors...")
			print("You are instantly struck down by a bolt of lightning, obliterating you into dust.")
	
	else:
		print("\nYou begin swimming...")
		print("A giant trout appears in your path, proceeding to swallow you whole in one fell swoop.")

else:
	print("\nYou turned right...")
	print("You fall straight into a massive hole in the ground, plummeting to your doom.")

print("\nTHE END!\n")
