# This script will accept inputs from the user about how many letters, symbols,
# and numbers to include and then generate a random password according to their
# specifications
#
# Created by: Lohit Deva
# 09/12/2022

import random

print("\nWelcome to the PyPassword Generator")

# Storing as string instead of list takes up considerably less space in memory
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!#$%&()*+'

no_letters = int(input("\nHow many letters do you want in the password?\n"))
no_numbers = int(input("How many numbers do you want in the password?\n"))
no_symbols = int(input("How many symbols do you want in the password?\n"))

# Here we use random.choices() to pick some items from an iterable (with replacement). The parameter
# k has to be specified to denote how many items to pick.
#
# Since lists are returned, we append them directly with each other to reduce creating extra variables.
raw_chars = random.choices(letters, k=no_letters) + random.choices(numbers, k=no_numbers) + random.choices(symbols, k=no_symbols)

# random.shuffle() shuffles the list in place, thereby eliminating the need to create a new list.
# To create a new list, we can use random.sample()
random.shuffle(raw_chars)

# Here, a for loop is added to concatenate all the characters in the list into a string
password = ''
for char in raw_chars:
	password += char

print(f"\nYour new password is {password}\n")	
