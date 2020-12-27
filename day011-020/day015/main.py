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


def print_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_drink_exists(order):
    return order in MENU


def check_resources_sufficient(drink):
    ingredients = drink["ingredients"]
    if resources["water"] < ingredients["water"]:
        print("Sorry there is not enough water.")
        return False

    if "milk" in ingredients:
        if resources["milk"] < ingredients["milk"]:
            print("Sorry there is not enough milk.")
            return False

    if resources["coffee"] < ingredients["coffee"]:
        print("Sorry there is not enough coffee.")
        return False

    return True


def process_coins(cost):
    print("Please insert coins.")
    num_quarters = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))
    num_nickles = int(input("how many nickles?: "))
    num_pennies = int(input("how many pennies?: "))
    total = 0.25 * num_quarters + 0.1 * num_dimes + \
        0.05 * num_nickles + 0.01 * num_pennies
    if total >= cost:
        if total - cost > 0:
            print(f"Here is ${total - cost} in change.")
        return cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def make_coffee(drink):
    global resources
    ingredients = drink["ingredients"]
    if "water" in ingredients:
        resources["water"] -= ingredients["water"]

    if "milk" in drink:
        resources["milk"] -= ingredients["milk"]

    if "coffee" in drink:
        resources["coffee"] -= ingredients["coffee"]


def coffee_machine():
    money = 0

    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")

        if order == "off":
            break

        if order == "report":
            print_report(money)
        elif check_drink_exists(order):
            drink = MENU[order]
            if not check_resources_sufficient(drink):
                continue

            processed_money = process_coins(drink["cost"])
            if processed_money == 0:
                continue

            money += processed_money
            make_coffee(drink)
            print(f"Here is your {order} ☕️ Enjoy!")


coffee_machine()
