
MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # TODO: Write this section so the program converts F to C and displays the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()


