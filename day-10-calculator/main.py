# This script accepts two numbers and an operator from the user and performs the desired arithmetic calculation.
# The script also allows the user to continue a given calculation, or to start a new one.

import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def compute(num1, num2, operator):
    '''
        This function accepts two numbers and an operator from the user and outputs the result of the 
        desired arithmetic operation.
    '''
    # The eval keyword allows you to evaluate Python expressions from string based inputs
    return eval(f'{num1} {operator} {num2}')

def pickOperator():
    '''
        This function displays the allowed set of operations to a user and asks the user to pick one and returns the selected operator.
        If the user picks an invalid option, they are allowed to pick again until they make a valid choice.
    '''
    operators = ['+', '-', '*', '/']
    operator = ''
    print('\n', *operators, sep='\n')
    while operator not in operators:
        operator = input("\nPick an operation\n")
        if operator not in operators:
            print("Invalid option, please try again\n")
    return operator

continue_condition = 'n'

num1, num2, result = 0, 0, 0

while continue_condition == 'n' or continue_condition == 'y':
    
    # This condition denotes the start of a new calculation
    if continue_condition == 'n':
        os.system('cls')
        print(logo)
        num1 = float(input("\nWhat's the first number?\n"))

    # This condition denotes the continuation of a current calculation
    else:
        num1 = result

    operator = pickOperator()
    num2 = float(input("\nWhat's the next number?\n"))
    result = compute(num1, num2, operator)
    print(f'{num1} {operator} {num2} = {result}')

    continue_condition = input(f'Type \'y\' to continue calculating with {result}, type \'n\' to start a new calculation, or type anything else to end the calculation\n').lower()

print("\nYou have exited the calculator, goodbye!\n")