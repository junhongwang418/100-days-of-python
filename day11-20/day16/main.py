from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        order = input(f"What would you like? ({menu.get_items()}): ")

        if order == "off":
            break

        if order == "report":
            coffee_maker.report()
            money_machine.report()
            continue

        drink = menu.find_drink(order)

        if drink == None:
            continue

        if not coffee_maker.is_resource_sufficient(drink):
            continue

        if not money_machine.make_payment(drink.cost):
            continue

        coffee_maker.make_coffee(drink)


coffee_machine()
