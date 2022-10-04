import math

def money_split():
    date = input("What is todays date?: ")
    x = float(input("How much did you make this week?: "))
    re
    savings = x * 0.5
    life_spending = x * 0.3
    personal_spending = x * 0.2
    total = savings + life_spending + personal_spending
    with open("/Users/tedputman/Desktop/savings/how much save.txt", "a+") as save:
        save.write(f"You made {x} on {date}:\n")
        save.write(f"{savings} in savings\n")
        save.write(f"{life_spending} for existing\n")
        save.write(f"{personal_spending} for personal spending")
        save.write(f"and $500 for rent")

   