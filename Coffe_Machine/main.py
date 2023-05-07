from menu import Menu, MenuItem
from Coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"Apa yang kamu suka ? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffe_maker.is_resource_sufficient(drink)
        is_payment_succesful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_succesful:
            coffe_maker.make_coffee(drink)
        
        