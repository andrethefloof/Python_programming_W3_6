print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")
print()
if choice == "1":
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    choicelength = input("Your choice: ")
    if choicelength == "1":
        meters = float(input("Insert meters: "))
        kilometers = round(meters / 1000)
        print(f"{meters} m is {kilometers} km")
        print()
    elif choicelength == "2":
        kilometers = float(input("Insert kilometers: "))
        meters = round(kilometers * 1000)
        print(f"{kilometers} km is {meters} m")
        print()
    elif choicelength == "0":
        print("Exiting...")
        print()
    else:
        print("Unknown option.")
        print()
elif choice == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    choiceweight = input("Your choice: ")
    if choiceweight == "1":
        grams = float(input("Insert grams: "))
        pounds = round(grams / 453.59237)
        print(f"{grams} g is {pounds} lb")
        print()
    elif choiceweight == "2":
        pounds = float(input("Insert pounds: "))
        grams = round(pounds * 453.59237)
        print(f"{pounds} lb is {grams} g")
        print()
    elif choiceweight == "0":
        print("Exiting...")
        print()
    else:
        print("Unknown option.")
        print()
elif choice == "0":
    print("Exiting...\n")
else:
    print("Unknown option.\n")
print("Program ending.")