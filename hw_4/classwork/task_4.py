user_input = int(input("Please enter file size in gigabytes: "))

if user_input in range(1, 1025):
    internet_bites_speed = int(input("Please enter internet speed in bites per second: "))

    megabytes = internet_bites_speed / (8 * 1024**2)

    print(f"")

    user_choice = input("Please enter 1(to calculate how many hours a file will be downloading)\n"
                        "             2(to calculate how many minutes a file will be downloading)\n"
                        "             3(to calculate how many seconds a file will be downloading): ")

    formula = 1024 / megabytes * user_input

    if user_choice == "1":
        print(f"\n{round(formula / 3600, 2)} hours remaining to download {user_input} GB")

    elif user_choice == "2":
        print(f"\n{round(formula / 60, 2)} minutes remaining to download {user_input} GB")

    elif user_choice == "3":
        print(f"\n{round(formula, 2)} seconds remaining to download {user_input} GB")

    else:
        print("\nYour input isn't equal 1, 2 or 3.")

else:
    print("Your input must be in range from 1 to 1024.")
