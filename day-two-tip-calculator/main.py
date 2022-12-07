# Python script to accept a bill amount, a tip percentage, number of people to be divided among
# and then output the amount that each person has to pay.
# 
# Created by: Lohit Deva
# 07/12/2022

print("Welcome to the tip calculator")
bill_amount = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people_number = int(input("How many people to split the bill? "))

# First the total amount is calculated inclusive of tip, then it is split among the
# number of people, and finally the round function is used to round it to two decimal places
split = round(((bill_amount + (tip/100) * bill_amount) / people_number), 2)

print(f'Each person should pay: ${split}')
