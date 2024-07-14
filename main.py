import report
list = ["espresso", "report", "cappuccino", "black"]
espresso_1 = 0

while True:
    print("What drink would you like?")
    a = input()
    if a == "report":
        report.report()

    if a not in list:
        print("We don't have that, try again")
    else:
        break

if a == "espresso":
    espresso_1 += 2
    print("You chose espresso, would you like it with sugar? (yes/no)")
    state_1 = input()
    if state_1 == "yes":
        print("Espresso with sugar chosen")
        espresso_1 += 2
    elif state_1 == "no":
        print("Espresso without sugar chosen")

    print("Would you like a cake with your espresso? (yes/no)")
    state_2 = input()
    if state_2 == "yes":
        print("Which cake? Choices are eclair and macaron")
        state_3 = input()
        if state_3 == "eclair":
            espresso_1 += 2
        elif state_3 == "macaron":
            espresso_1 += 4
    elif state_2 == "no":
        print("Espresso without cake chosen")
elif a == "report":
    print("Espresso 200ml")
    print("Other coffee 300ml")
else:
    print("Coffee")

print(f"GREAT, no problem, your order total is {espresso_1}")
