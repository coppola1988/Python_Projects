from menu_coffemachine import MENU, resources
from coffe_art import logo
import time


def countdown(seconds, choose):
    print(f"Here comes your {choose}")
    while seconds > 0:
        if seconds == 1:
            print(f"{seconds} sekunde ...")
        else:
            print(f"{seconds} sekunden ...")
        time.sleep(1)
        seconds -= 1


def flavour(choose1):
    """returns the remaining resources or an error1 if not enough resources"""
    water = MENU[choose1]["ingredients"]["water"]
    coffee = MENU[choose1]["ingredients"]["coffee"]

    if resources["water"] < water:
        print("Sorry not enough water ")
        return "error1"

    elif resources["coffee"] < coffee:
        print("Sorry not enough coffee")
        return "error1"

    resources["water"] -= water
    resources["coffee"] -= coffee

    if choose1 == "latte" or choose1 == "cappuccino":
        milk = MENU[choose1]["ingredients"]["milk"]
        if resources["milk"] < milk:
            print("Sorry not enough milk")
            return "error1"
        resources["milk"] -= milk
    return resources


def calculating(cost):
    """Calculate the given coins and returns the change"""
    bank = 0

    for key in coins:
        try:
            amount = int(input(f"How many {key}: "))
            if amount < 0:
                raise ValueError("The number of coins cannot be negative.")
            pay_amount = coins[key] * amount
            bank += pay_amount
        except ValueError as ve:
            print(f"Invalid input: {ve}")
            return "error3"
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return "error3"
    if bank < cost:
        print("Sorry not enough money. Money refunded.")
        return "error2"
    else:
        change = bank - cost
        return change


coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}
turn_on = True
money = 0
print(logo)
while turn_on:

    print("Welcome Customer!")
    choose = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choose == "report":
        water = resources["water"]
        coffee = resources["coffee"]
        milk = resources["milk"]
        print(f"Water: {water}\nCoffee: {coffee}\nMilk: {milk}")
        print(f"Money: {money}")
    elif choose == "off":
        print("Coffe machine turns off. Good Bye!")
        turn_on = False
    else:
        resource = flavour(choose)

        if resource != "error1":
            print("Please insert coins. ")
            price = MENU[choose]["cost"]
            money += price
            exchange = calculating(price)
            if exchange != "error2" and exchange != "error3":
                print(f"Here is {round(exchange, 2)} in change")
                countdown(5, choose)
                print(f"Here is your {choose} ☕ Enjoy!\n")
