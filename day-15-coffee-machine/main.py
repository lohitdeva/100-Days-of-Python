# Created by: Lohit Deva
# 29/12/2022

# Menu dictionary containing available beverage options along with their cost and ingredients.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Resources dictionary containing the available resources inside the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True
profit = 0.0


def check_items(menu):
    '''
    Accepts a list of items and returns a formatted string listing out the different items.\n
    For example: check_items([apple, orange]) => (apple/orange)
    '''
    items_string = ''
    for item, item_details in menu.items():
        items_string += f"{item.title()} - ${item_details['cost']}\n"
    return items_string


def generate_report(resources, profit):
    '''
    Accepts a dictionary of remaining resources and returns a formatted string which lists
    all the different key value pairs in the dictionary.
    '''
    report_string = '\n'
    # Iterates through list of available key value pairs in the resources dictionary and formats the string in the
    # form key: value, where key is converted to title case. A check is also carried out to add a 'g' suffix if the key
    # is coffee and 'ml' for any other item.
    for k, v in resources.items():
        report_string += (f"{k.title()}: {v}{'g' if k == 'coffee' else 'ml'}\n")
    report_string += (f"Profit: ${profit}\n")
    return report_string


def resource_check(item, menu, resources):
    '''
    Accepts an item as a string, menu and resources as dictionary and returns a boolean after evaluating
    if there are sufficient resources to prepare the specified item from the menu.
    '''
    # Iterates through the different available resources. Once a resource is obtained, it also checks if that same resource
    # is required as an ingredient for the beverage. If required, one final check is carried out to check if there is sufficient
    # quantity to prepare the beverage.
    for resource in resources.keys():
        if resource in list(menu[item]['ingredients']): 
            if resources[resource] < menu[item]['ingredients'][resource]:
                print(f"\nNot enough {resource}. Sorry for the inconvenience\n")
                return False
    return True


def coins_paid():
    '''
    Accepts user inputs for different types of coins paid and returns a dictionary with the compiled set of coin values.
    '''
    coins = {
        "quarters": 0,
        "dimes": 0,
        "nickels": 0,
        "pennies": 0
    }
    
    print("\nPlease insert coins")
    
    for k in coins.keys():
        coins[k] = int(input(f"How many {k}? "))
        
    return coins


def money_paid(coins):
    '''
    Accepts a coin dictionary as input and returns the actual amount paid by user.
    '''
    return coins['quarters'] * 0.25 + coins['dimes'] * 0.1 + coins['nickels'] * 0.05 + coins['pennies'] * 0.01


def check_transaction(coins, item, menu):
    '''
    Accepts coin dictionary, item string, and menu dictionary as inputs and verifies if the user input
    enough coins to pay for their item of choice. If the cost of the item is satisfied, any change (if available) is
    returned to the user. If not, the whole amount is refunded.
    '''
    amt = money_paid(coins)
    
    if amt >= menu[item]['cost']:
        print()
        if amt > menu[item]['cost']:
            print(f"Here is ${amt - menu[item]['cost']:.2f} in change")
        return True
    else:
        return False
    

def update_resource(menu, resources, item):
    '''
    Accepts menu and resources dictionaries and item string and returns an updated resource dictionary
    after deducting the amount of ingredients required to make the users beverage of choice
    '''
    for ingredient in menu[item]['ingredients'].keys():
        resources[ingredient] -= menu[item]['ingredients'][ingredient]
    return resources
    
            
def run_machine(menu, resources, machine_on, profit):
    '''
    Accepts a dictionary of menu items, dictionary of available resources, and variable about machine state
    and runs the coffee machine accordingly.
    '''
    items = list()
    
    # Appends all different options available items on the menu into a list
    for _ in menu:
        items.append(_)
    
    while machine_on:
        choice = input(f"What would you like?\n{check_items(menu)}").strip().lower()
        
        # Checks if user has input a valid option
        while choice not in items and choice != 'off' and choice != 'report':
            choice = input(f"That item is not available, please try something from our menu. {check_items(items)}\n").strip().lower()
        
        if choice == 'off':
            machine_on = False
            continue
        elif choice == 'report':
            print(generate_report(resources, profit))
            continue
        
        if not resource_check(choice, menu, resources):
            continue
        
        coins = coins_paid()
        
        if not check_transaction(coins, choice, menu):
            print("\nSorry that's not enough money. Money refunded.\n")
            continue
        
        print(f"Here is your {choice} ☕. Enjoy 😃\n")
        
        resources = update_resource(menu, resources, choice)
        profit += menu[choice]['cost']
        
        
    print("\nMachine is now powered off\n")
   
    
run_machine(MENU, resources, machine_on, profit)