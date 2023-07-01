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


# Print Report
def report():
  for x in resources:
     print(f"{x} : {resources[x]}")

# Check Resources Sufficient
def resources_suf(user_choice):
  for x in MENU[user_choice]["ingredients"]:
    if resources[x] < MENU[user_choice]["ingredients"][x]:
      print(f"Sorry, you don't have enough {x}")
      return False
  return True
  
# process coin
def process_coin():
  print("Insert a coin, please")
  # A penny is worth 1 cent.
  amt = int(input("How many pennies?: ")) * 0.01
  # A nickel is worth 5 cents.
  amt += int(input("How many nickels?: ")) * 0.05
  # A dime is worth 10 cents.
  amt = int(input("How many dime?: ")) * 0.10
  # A quarter is worth 25 cents.
  amt += int(input("How many quarters?: ")) * 0.25
  return amt

# transaction success
def transaction_success(x, amt_total):
  if amt_total >= MENU[x]["cost"]:
    amt_change = amt_total - MENU[x]["cost"]
    for y in MENU[x]["ingredients"]:
      if y in resources:
        resources[y] -= MENU[x]["ingredients"][y]

    print(f"Your {x} is ready ☕ \n")
    print(f"Here is ${round(amt_change, 2)} dollars in change.")
  else:
    print("Sorry that's not enough money. Money refunded..")



# Make Coffeeo

still_operating = True

while still_operating:
  user_choice = input("What would you like? espresso/latte/cappuccino): ").lower()
  
  if user_choice == "report":
    report()
  elif user_choice == "off":
    still_operating = False
  else:
    if resources_suf(user_choice) == True:
      amt_total = process_coin()
      transaction_success(user_choice, amt_total)
      

