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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}

is_on = True


def available_resources(oder_ingredients):
    for item in oder_ingredients:
        if oder_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough{item}")
            return False
    return True


def coin_total():
    print("Please insert coins? ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dime? ")) * 0.1
    total += int(input("How many nickel? ")) * 0.05
    total += int(input("How many penny? ")) * 0.01

    return total


def money_transacted_is_enough(total_paid, drink_cost):
    if total_paid >= drink_cost:
        global profit
        change = round(total_paid - drink_cost, 2)
        print(f"Your change is ${change}")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.Money refunded")
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print("You can have your coffee")


while is_on:
    decision = input("What would you like? (espresso/latte/cappuccino):")
    if decision == "off":
        is_on = False
    elif decision == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit: ${profit}")
    else:
        drink = MENU[decision]
        if available_resources(drink["ingredients"]):
            payment = coin_total()
            if money_transacted_is_enough(payment, drink["cost"]):
                make_coffee(decision, drink["ingredients"])
