from pop import resources
from pop import MENU


def report(money):
    print(f"Water = {resources["water"]}")
    print(f"Mik = {resources["milk"]}")
    print(f"Coffee = {resources["coffee"]}")
    print(f"Money = {money}")


def process_money(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    total = float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)

    if total< MENU[drink]["cost"]:
        print("Sorry that's not enough money . Money refunded")
        return 0
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappucino":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    print(f"Here is {(total - MENU[drink]["cost"]): .2f} dollars in change")
    print(f"Here is your {drink} enjoy")
    return MENU[drink]["cost"]

def check_resources(drink):
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Not enough Water")
        return False
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Not enough Coffee")
        return False
    if drink == "latte" or drink == "cappucino":
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Not enough Milk")
            return False
    return True


def coffe_machine():
    money = 0.0
    while (True):
        inp = input("What would you like? (espresso,latte,cappucino):")

        match inp:
            case "report":
                report(money)

            case "espresso":
                if not (check_resources(inp)):
                    break
                money += process_money(inp)
            case "latte":
                if not (check_resources(inp)):
                    break
                money += process_money(inp)
            case "cappucino":
                if not (check_resources(inp)):
                    break
                money += process_money(inp)

            case "off":
                print("Goodbye")
                break


coffe_machine()
