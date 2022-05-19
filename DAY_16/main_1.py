from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

print("Welcome to the coffee machine")
is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"Which drink would you want take {option}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
        is_money_sufficient = money_machine.make_payment(drink.cost)
        if is_resource_sufficient and is_money_sufficient:
            print(coffee_maker.make_coffee(drink))
