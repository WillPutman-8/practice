#This bot should create an easy to follow savings plan every pay-check:

personal = float(input("How much did you get paid this period: $"))
rent = 325 /2
need = 200
gas = 120
bill_due = input("is the power bill due (Y/N)").lower()

if bill_due == "y":
    power = float(input("How much is the power bill: $"))
    power /= 2
    dylan_power = power -25
    will_power = power + 25
    print(f"Dylan owes ${dylan_power} and I owe ${will_power} for the power bill.")
    personal -= will_power

personal -= rent
personal -= need
personal -= gas
save = personal * 0.5
personal -= save
print(f"you have ${personal} for personal spending, and you should move ${save} into your savings!")