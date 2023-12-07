cost = float(input("Please enter cost of one game console: "))
quantity = int(input("Please enter quantity of game consoles: "))
discount = int(input("Please enter percentage discount(0% - 100%): "))

user_choice = input("Please enter 1(to sum all consoles)\n"
                    "             2(to calculate price of one console with discount): ")

if discount not in range(0, 101):
    print("Discount must be in range from 0 to 100.")
else:
    if user_choice == "1":
        print(f"Price of {quantity} consoles is: {cost * quantity}")
    elif user_choice == "2":
        print(f"Price of one console with discount is: {cost * (1 - (discount * 0.01))}")
    else:
        print("Your input isn't equal 1 or 2.")
