from math import pi

diameter = float(input("Please enter diameter of circle: "))
user_action = input("Please enter 1(to solve square of circle)\n"
                    "             2(to solve perimeter of circle): ")

if user_action == "1":
    print(f"Square: {round(pi * ((diameter / 2) ** 2), 3)}")

elif user_action == "2":
    print(f"Perimeter: {round(pi * diameter, 3)}")

else:
    print("Your input isn't 1 or 2")
