
import report
list = ["ekspresso", "report", "capuccio", "czarna"]
ekspresso_1 = 0

while True:
    print("Jak chcesz napój? ")
    a = input()
    if a == "report":
        report.report()

    if a not in list:
        print("tego nima, dawaj dalej")
    else:
        break

if a == "ekspresso":
    ekspresso_1 += 2
    print("Wybrales ekspresso, czy chcesz z cukrem? (tak/nie)")
    state_1 = input()
    if state_1 == "tak":
        print("Wybrano ekspresso z cukrem")
        ekspresso_1 += 2
    elif state_1 == "nie":
        print("Wybrano ekspresso bez cukru")

    print("Czy chcesz ciasto do ekspresso? (tak/nie)")
    state_2 = input()
    if state_2 == "tak":
        print("Jakie ciastko? Wybór to ptys i omaga")
        state_3 = input()
        if state_3 == "ptys":
            ekspresso_1 += 2
        elif state_3 == "omaga":
            ekspresso_1 += 4
    elif state_2 == "nie":
        print("Wybrano ekspresso bez ciastka")
elif a == "report":
    print("Ekspresso 200ml")
    print("Kawkiem inna 300ml")
else:
    print("Kawkiem")

    print(f"SIUPER nie bedzie pania, Twoje zamówienie wynosi {ekspresso_1}")
