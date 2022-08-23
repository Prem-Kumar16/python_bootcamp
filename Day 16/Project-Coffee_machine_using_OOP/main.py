from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO : 1. Prompt user by asking "What would you like? "
# TODO : 2. Turn off the machine by using OFF from prompt
# TODO : 3. Print report
# TODO : 4. Check resources sufficient?
# TODO : 5. Process coins
# TODO : 6. Check transaction successful
# TODO : 7. Make coffee


resources_present = CoffeeMaker()

menu = Menu()
is_on = True

money_machine = MoneyMachine()

while is_on:
    option = menu.get_items()
    user_option = input(f"What do you wanna drink? {option} : ")
    if user_option == "off":
        is_on = False
    elif user_option == "report":
        resources_present.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_option)
        if resources_present.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                resources_present.make_coffee(drink)
