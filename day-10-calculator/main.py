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
    return eval(f'{num1} {operator} {num2}')

def pickOperator():
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
    if continue_condition == 'n':
        os.system('cls')
        print(logo)
        num1 = float(input("\nWhat's the first number?\n"))

    else:
        num1 = result

    operator = pickOperator()
    num2 = float(input("\nWhat's the next number?\n"))
    result = compute(num1, num2, operator)
    print(f'{num1} {operator} {num2} = {result}')

    continue_condition = input(f'Type \'y\' to continue calculating with {result}, type \'n\' to start a new calculation, or type anything else to end the calculation\n').lower()

print("\nYou have exited the calculator, goodbye!\n")