from data import MENU
from data import resources

def coffee_mahcine():
    print("Welcome to COFFEE MACHINE")
    order = input("What would you like? (espresso, latte, cappuccino): ").lower()


    if order == "report":
        print(resources)
        return True
    elif order == "off":
        return False
    else:
        print(f"{order}: ${MENU[order]['cost']}")

        cost = MENU[order]["cost"]

    if resources["water"] <= MENU[order]["ingredients"]["water"] and resources["milk"] <= MENU[order]["ingredients"]["milk"] and resources["coffee"] <= MENU[order]["ingredients"]["coffee"]:
        print("Coffee Machine is out of ingredients please refill.")
        print(resources)
        return False
    elif resources["water"] <= MENU[order]["ingredients"]["water"]:
        print("Not enough water to make order.")
        print(resources)
        return True
    elif resources["milk"] <= MENU[order]["ingredients"]["milk"]:
        print("Not enogh milk to make order.")
        print(resources)
        return True
    elif resources["coffee"] <= MENU[order]["ingredients"]["coffee"]:
        print("Not enough coffee to make order")
        print(resources)
        return True

    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["milk"] -= MENU[order]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
# change values
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    print("Please insert payment.")
    q_amount = int(input("How many quarters?: ")) * quarters
    d_amount = int(input("How many dimes?: ")) * dimes
    n_amount = int(input("How many nickles?: ")) * nickles
    p_amount = int(input("How many pennies?: ")) * pennies

    total_paid = q_amount + d_amount + n_amount + p_amount

    if total_paid < cost:
        print(f"Insuficiant funds. Change returned: {total_paid}")
        return True
    else:
        total_paid -= cost
        resources["money"] = cost
        print(f"your change is {total_paid}")
        print(f"Here is your {order}. Enjoy!")
        return True






x = True
while x:
    x = coffee_mahcine()