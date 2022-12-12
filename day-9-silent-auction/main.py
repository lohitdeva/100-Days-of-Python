# This program emulates a silent auction where users make bids silently, i.e, without revealing their bids. In the end, the 
# person with the highest bid among all the bidders is crowned the winner.

# This module allows us to use the system() function to send commands directly to the system's terminal window.
import os

# This function creates a new bidder by creating a dictionary with two entries having the keys 'name' and 'bid'.
# The function returns the created dictionary back to the calling function.
def create_bidder():
	new_bidder = {}
	new_bidder["name"] = input("\nWhat is your name?\n")
	new_bidder["bid"] = input("What is your bid?\n$")
	return new_bidder

print(r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

# Initializing an empty list of bidders
bidders = []
# Creating the first entry into the list of bidders by directly appending the dictionary returned by the create_bidder() function.
bidders.append(create_bidder())

continue_bid = input("\nAre there more bidders? Type 'yes' or 'no'.\n").lower().strip()

# Creating a loop that continues to run and create more entries into the list of bidders as long as the continue_bid variable is set to 'yes'.
while continue_bid == 'yes':
	os.system('cls')
	bidders.append(create_bidder())
	continue_bid = input("\nAre there any more bidders? Type 'yes' to proceed or anything else to exit\n").lower().strip()

# Here, the system() function from the os module directly sends the 'cls' command to the Windows terminal to clear the screen.
# NOTE: use 'clear' for MacOS and Linux machines.
os.system('cls')

# Originally, the bid value of the first bidder is set as the highest and the pos variable is used to identify the location
# of the bidder in the list of bidders
highest_bid = bidders[0]['bid']
pos = 0

# In this loop, the highest_bid is computed by the current bid to the immediate neighbour.
for i in range(1, len(bidders)):
	if highest_bid < bidders[i]['bid']:
		highest_bid = bidders[i]['bid']
		pos = i

# The winner of the silent auction is declared.
print(f'The winner is {bidders[pos]["name"]} with a bid of ${bidders[pos]["bid"]}\n')		
