# This Python script recreates the ancient Caesar cipher. In the Caesar cipher, a given piece of plaintext is encoded
# by shifting it down a certain number of places down the alphabet. The number of characters to be shifted by is predetermined
# and mutually agreed upon by the sender and receiver. Decoding the Caesar cipher works by simply going up the alphabet the
# same number of characters it was shifted down by.
#
# Created by: Lohit Deva
# 11/12/2022

# This function is to encode a given string using the Caesar cipher. The 'raw' parameter is the string that is to be encoded and
# the 'shift' parameter is the number of characters it has to be shifted down the alphabet by.
def encodeString(raw, shift):
	result = ''
	
	# This loop goes through every character in the original string and shifts it.
	for char in raw:

		# The loop simply adds a blank to the resultant string and skips any computation if a blank space is encoutered.
		if not char.isalnum() :
			result += char
			continue

		# This checks if the character is an alphabet and thus uses the alphabets string as reference.
		elif char.isalpha():
		
			# Here, position after shifting is calculated. The modulo operator is used to ensure that position oof shifted
			# character stays between 0 - 25 (the available indices in the alphabets string).
			# Since we are shifting the position of the character down the alphabet, we add shift.
			position = (alphabets.index(char.lower()) + shift) % len(alphabets)
		
			# This checks if the character in the original string is upper case and maintains the case.
			if char.isupper():
				result += alphabets[position].upper()
		
			# If it is not uppercase, then the character is simply appended without modification.
			else:
				result += alphabets[position]

		# This executes if the character is a number and uses the numbers string as reference.
		else:		
			
			result + = numbers[(numbers.index(char) + shift) % len(numbers)]

	print(f"\nThe encoded string is: {result}\n")	

# This function works similar to the encodeString() function, except that it moves the characters up the alphabet by the 
# specified number of shifts and thus can decode a cipher created by the encodeString() function if the same shift is used.
def decodeString(raw, shift):
	result = ''
	
	for char in raw:

		if not char.isalnum() :
			result += char
			continue

		# Here we subtract shift since we are moving up the alphabet. 
		elif char.isalpha():
		
			position = (alphabets.index(char.lower()) - shift) % len(alphabets)
		
			if char.isupper():
				result += alphabets[position].upper()
		
			else:
				result += alphabets[position]

		else:		
			
			result + = numbers[(numbers.index(char) - shift) % len(numbers)]

	print(f"\nThe encoded string is: {result}\n")	

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
			encodeString(raw_string, shift)

		else:
			decodeString(raw_string, shift)

	# Here the condition for the while loop is updated. If the user enters 'y' (or 'Y'), the initial condition stays true
	# and the loop continues for another iteration. However if any different input is entered, the loop is immediately terminated.
	loop_continue = input("Do you want to continue using the Caesar cipher generator? Press 'y' or 'Y' to continue, press anything else to exit\n").strip().lower()
