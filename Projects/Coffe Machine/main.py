from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

profit = 0

on = True
coffe_maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while on:

    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        print("Exiting")
        on = False

    elif choice == "report":
        coffe_maker.report()
        money.report()
            
    else:
        drink = menu.find_drink(choice)

        if coffe_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)

        
    
             

