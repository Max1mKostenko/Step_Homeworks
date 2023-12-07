operator_rates = {
    "Vodafone": 1.0,
    "Kyivstar": 1.2,
    "Lifecell": 1.5,
}

try:
    duration = float(input("Please enter duration of ring in minutes: "))
    operator_code = input("Please enter mobile operator (Vodafone, Kyivstar, Lifecell): ").capitalize()

    if operator_code not in operator_rates:
        print("Error: nonexistent operator")

    else:
        cost = duration * operator_rates[operator_code]
        print(f"Price of call: {cost} uah.")
except ValueError:
    print("You must enter correct phone calling duration.")
