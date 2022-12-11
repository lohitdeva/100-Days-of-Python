# This Python script recreates the ancient Caesar cipher. In the Caesar cipher, a given piece of plaintext is encoded
# by shifting it down a certain number of places down the alphabet. The number of characters to be shifted by is predetermined
# and mutually agreed upon by the sender and receiver. Decoding the Caesar cipher works by simply going up the alphabet the
# same number of characters it was shifted down by.
#
# Created by: Lohit Deva
# 11/12/2022

def caesar(raw, shift, direction):

	# Initialized an empty string to store the result.
	result = ''

	# Changing the shift to negative in case of decode as the shifting needs to move up the alphabet (or numbers) instead
	# of down
	if direction == 'd':
		shift = -shift

	for char in raw:

		# If the character is not an alphabet or number, it can just be added to the result string as is.
		if not char.isalnum():
			result += char
			continue

		else:
			# In case of alphabet characters, the 'alphabets' string needs to be used to shift the character.
			if char.isalpha():
				position = (alphabets.index(char.lower()) + shift) % len(alphabets)

				# This ensures that any uppercase character remains uppercase after shifting
				if char.isupper():
					result += alphabets[position].upper()
				else:
					result += alphabets[position]

			# In case of numeric characters, the 'numbers' string needs to be used to shift the characters.
			else:
				result += numbers[(numbers.index(char) + shift) % len(numbers)]
	
	# Here we use a ternary operation to display the appropriate text based on the conversion that was carried out.
	print(f'Your {"encoded" if direction == "e" else "decoded"} text is: {result}')

# This string contains the letters of the alphabet to use as a reference when shifting characters while encoding/decoding.
alphabets = 'abcdefghijklmnopqrstuvwxyz'
# This string contains the digits from 0-9 and will be used while encoding/decoding numbers.
numbers = '0123456789'

print('''
░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀
''')		

print("\nWelcome to the Caesar cipher generator\n")

# This variable is to validate the condition of the while loop.
loop_continue = 'y'

while loop_continue == 'y':
	
	choice = input("\nTo proceed, enter 'encode' to encode a string or 'decode' to decode a string\n").lower().strip()


	# Entering an invalid input does not terminate the program but just sends the user back to the encode/decode screen.
	if choice != 'encode' and choice != 'decode':
		print('\nYou entered an invalid input, please try again\n')
		continue

	else:
		raw_string = input("\nEnter the string:\n")
		shift = int(input("Enter the number of characters to be shifted by:\n"))

		if choice == 'encode':
			caesar(raw_string, shift, 'e')

		else:
			caesar(raw_string, shift, 'd')

	# Here the condition for the while loop is updated. If the user enters 'y' (or 'Y'), the initial condition stays true
	# and the loop continues for another iteration. However if any different input is entered, the loop is immediately terminated.
	loop_continue = input("Do you want to continue using the Caesar cipher generator? Press 'y' or 'Y' to continue, press anything else to exit\n").strip().lower()
