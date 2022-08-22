MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def coins(user_option, menu):
    price = menu[user_option]["cost"]

    print("Please insert coins")
    quarter = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarter * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if total > price:
        change = round(total - price, 2)
        print(f"Here is ${change} in change")
        print(f"Here is your {user_option}, Enjoy")
        global money
        money += (total - change)
    else:
        print("Insufficient amount. Amount refunded")


def resource_check(user_option, menu, resources_present):
    water_needed = menu[user_option]["ingredients"]["water"]
    milk_needed = menu[user_option]["ingredients"]["milk"]
    coffee_needed = menu[user_option]["ingredients"]["coffee"]
    water_left = resources_present["water"]
    milk_left = resources_present["milk"]
    coffee_left = resources_present["coffee"]

    if water_left >= water_needed and milk_left >= milk_needed and coffee_left >= coffee_needed:
        resources_present["water"] -= water_needed
        resources_present["milk"] -= milk_needed
        resources_present["coffee"] -= coffee_needed
        coins(user_option, menu)
        return True
    elif water_left < water_needed:
        print("Sorry, there is not enough water left")
        return False
    elif milk_left < milk_needed:
        print("Sorry, there is not enough milk left")
        return False
    else:
        print("Sorry, there is not enough coffee powder left")
        return False


def making_process(user_option, menu, resources_present, earned):

    if user_option == "espresso":
        resource_check("espresso", menu, resources_present)
    elif user_option == "latte":
        resource_check("latte", menu, resources_present)
    elif user_option == "cappuccino":
        resource_check("cappuccino", menu, resources_present)
    else:
        print(f"Water left : {resources_present['water']} ml")
        print(f"Milk left : {resources_present['milk']} ml")
        print(f"Coffee powder left : {resources_present['coffee']} g")
        print(f"money : {round(earned, 2)} $")


# TODO : 1. Prompt user by asking "What would you like ? "
money = 0
machine_switch = True
while machine_switch:
    option = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if option == "off":
        machine_switch = False
    else:
        making_process(option, MENU, resources, money)
# TODO : 2. Turn off the coffee machine
# TODO : 3. Print report
# TODO : 4. Check if resources are sufficient ?
# TODO : 5. Process coins
# TODO : 6. Check transaction successful ?
# TODO : 7. Make coffee
