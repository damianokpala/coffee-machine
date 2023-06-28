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
    "money": 0.00,
}

def menu_check(x, amt_total):
  if amt_total >= MENU[x]["cost"]:
    amt_change = amt_total - MENU[x]["cost"]
    for y in MENU[x]["ingredients"]:
      if y in resources:
        resources[y] -= MENU[x]["ingredients"][y]

    print(f"Your {x} is ready ☕ \n")
    print(f"Here is ${round(amt_change, 2)} dollars in change.")
        
    #resources["money"] = amt_total - MENU[x]["cost"]
  else:
    print("Sorry that's not enough money. Money refunded..")
    

# Print Report
def report():
  for x in resources:
     print(f"{x} : {resources[x]}")

# print no report
def not_report():
  print("Insert a coin, please")
  # A penny is worth 1 cent.
  amt_penny = int(input("How many pennies?: ")) * 0.01
  # A nickel is worth 5 cents.
  amt_nickel = int(input("How many nickels?: ")) * 0.05
  # A dime is worth 10 cents.
  amt_dime = int(input("How many dime?: ")) * 0.10
  # A quarter is worth 25 cents.
  amt_quarter = int(input("How many quarters?: ")) * 0.25
  amt_total = amt_penny + amt_nickel + amt_dime + amt_quarter
  menu_check(user_choice, amt_total)
  
  




still_operating = True

while still_operating:
  user_choice = input("What would you like? espresso/latte/cappuccino): ").lower()
  
  if user_choice == "report":
    report()
  else:
    not_report()
  

# Check Resources Sufficient

# Process Coins

# Make Coffeeo