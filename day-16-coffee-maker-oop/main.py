# Remade the day 15 coffee maker script using OOP principles
# All files containing the required classes were supplied as part of the course
#
# Created by: Lohit Deva
# 29/12/2022

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()[:len(menu.get_items()) - 1]}) ").strip().lower()
    
    if choice == 'off':
        is_on = False
        
    elif choice == 'report':
        cm.report()
        mm.report()

    elif menu.find_drink(choice):
        beverage = menu.find_drink(choice)
        
        print(f"You have selected {beverage.name}")
        
        if cm.is_resource_sufficient(beverage):
            if mm.make_payment(beverage.cost):
                cm.make_coffee(beverage)