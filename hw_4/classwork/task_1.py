time = int(input("Please enter daytime in seconds: "))
if time not in range(0, 86400):
    print("The daytime in seconds is valid")

hours_1, minutes_1, seconds_1 = time // 3600, time % 3600 // 60, time % 3600 % 60

if hours_1 < 10:
    hours_1 = f"0{hours_1}"

elif minutes_1 < 10:
    minutes_1 = f"0{minutes_1}"

elif seconds_1 < 10:
    seconds_1 = f"0{seconds_1}"

print(f"Time now - {hours_1}:{minutes_1}:{seconds_1}")

rest = 86400 - time

hours_2, minutes_2, seconds_2 = rest // 3600, rest % 3600 // 60, rest % 3600 % 60

if hours_2 < 10:
    hours_2 = f"0{hours_2}"

elif minutes_2 < 10:
    minutes_2 = f"0{minutes_2}"

elif seconds_2 < 10:
    seconds_2 = f"0{seconds_2}"

print(f"Until midnight - {hours_2}:{minutes_2}:{seconds_2}")
