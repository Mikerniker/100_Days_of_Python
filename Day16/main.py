from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = 0
machine_open = True
coffee = CoffeeMaker()
ingred = MenuItem
menu = Menu()
process = MoneyMachine()

  
while machine_open:
    choice = input("What would you like? (espresso/latte/cappuccino)? ")
    if choice == "off":
        machine_open = False
    elif choice == "report":
      coffee.report()
      process.report()
    else: 
      drink = menu.find_drink(choice)
      if coffee.is_resource_sufficient(drink):
        # process.process_coins()
        if process.make_payment(drink.cost):
          coffee.make_coffee(drink)
