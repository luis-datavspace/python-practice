from prettytable import PrettyTable
resources_table = PrettyTable()
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    
    total = 0 
    print("Please insert coins.")
    total = int(input("How many quartes?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many niclkes?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total

def is_transaction_successful(money_received, drink_cost):
    
    if money_received >= drink_cost:
        change = round(money_received - drink_cost , 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name,order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")




    




profit = 0

on = True

while on:

    choice = ""

    while choice not in ["off","report","latte","espresso","cappuccino"]:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice not in ["off","report","latte","espresso","cappuccino"]:
            print("Please enter a valid option.")


    if choice == "off":
        print("Exiting")
        on = False

    elif choice == "report":
        resources_table.clear_rows()
        resources_table.field_names = ["Water","Milk","Coffee","Money"]
        resources_table.add_rows([

            [resources["water"],resources["milk"],resources["coffee"],f"${profit}"]
        ])
        print(resources_table)

    
    else:
        order = MENU[choice]
        if is_resources_sufficient(order["ingredients"]):
            money_received = process_coins()
            if is_transaction_successful(money_received, order["cost"]):
                make_coffe(choice, order["ingredients"])



    
    

        
