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
    
def water_needed(MENU, drink):
  waterin = MENU[drink]["ingredients"]["water"]
  return waterin
  

def milk_needed(MENU,drink):
  milkin = 0
  if drink != "espresso":
    milkin += MENU[drink]["ingredients"]["milk"]
    return milkin
  else:
    return milkin


def coffee_needed(MENU,drink):
  coffeein = MENU[drink]["ingredients"]["coffee"]
  return coffeein

def drink_cost(MENU, drink):
  """Accesses the cost of a drink"""
  cost = MENU[drink]["cost"]
  return cost  

def remaining_resources(resource, waterin, coffeein, milkin):
  """Calculates remaining resources after drink purchase"""
  global water, milk, coffee
  water -= waterin
  coffee -= coffeein
  milk -= milkin  
  return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: ${round(money):.2f}"


def customer_change(customers_money, cost_drink):
  """calculates customers change and puts the leftover in money"""
  global money
  change = customers_money - cost_drink
  money += cost_drink
  return f"Here is {change} in change."


def customer_deposit(quarter, dime, nickel, penny):
  """Calculate sum total of customers money"""
  quar = quarter * 0.25
  dim = dime * 0.10
  nick = nickel * 0.05
  pen = penny * 0.01  
  total = [quar, dim, nick, pen]
  return sum(total)  

#CALLS
money = 0 

#Available resources
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"] 


take_orders = True

while take_orders:
  
  drink = input("Welcome! What would you like? (espresso/latte/cappuccino): ")

  if drink == "report":
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${round(money):.2f}")

 
  else:  
  #check_resources
    if water <  water_needed(MENU, drink):
      print( f"Sorry not enough water.")
      take_orders = False
    elif coffee < coffee_needed(MENU,drink):
      print(f"Sorry not enough coffee.")
      take_orders = False
    elif milk < milk_needed(MENU,drink):
      print(f"Sorry not enough milk.")
      take_orders = False
    else:
        print("Please insert coins.")
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickel = int(input("How many nickels?: "))
        penny = int(input("How many pennies?: "))
        finaltotal = customer_deposit(quarter, dime, nickel, penny)
        print(f"Total coins is {finaltotal}")
  
     #Calculate change for customer
        if finaltotal > drink_cost(MENU, drink):
          changefor_customer = customer_change(customer_deposit(quarter, dime, nickel, penny), drink_cost(MENU, drink))
          print(changefor_customer)
          print(f"Here is your {drink}. Enjoy!")
        elif finaltotal < drink_cost(MENU, drink):
          print("Sorry that's not enough money. Money refunded.")
        else:
          print(f"Thank you for giving the exact amount! Here is your {drink}. Enjoy!")

# Check remaining resources
        remaining_resources(resources, water_needed(MENU, drink), coffee_needed(MENU,drink), milk_needed(MENU,drink))
 
