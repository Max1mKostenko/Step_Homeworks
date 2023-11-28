meter = float(input("Please enter any count of meters: "))

user_input = int(input("""Please enter 1(to convert into miles),
             2(to convert into inches ),
             3(to convert into yards): """))

if user_input == 1:
    print(f"{meter} meters in miles are {meter * 0.000621371}")

elif user_input == 2:
    print(f"{meter} meters in inches are {meter * 39.3701}")

elif user_input == 3:
    print(f"{meter} meters in yards are {meter * 1.09361}")

else:
    print("Number isn't 1 or 2 or 3")
