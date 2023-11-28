num1, num2, num3 = (int(input("Please enter first num: ")), int(input("Please enter second num: ")),
                    int(input("Please enter third num: ")))
user_operator = int(input("""Please enter 1(to find max),
             2(to find min),
             3(to find an arithmetic mean): """))

if user_operator == 1:
    print(f"Max of ({num1}, {num2}, {num3}): {max((num1, num2, num3))}")

elif user_operator == 2:
    print(f"Min of ({num1}, {num2}, {num3}): {min((num1, num2, num3))}")

elif user_operator == 3:
    print(f"Arithmetic mean of ({num1}, {num2}, {num3}): {round(sum((num1, num2, num3)) / 3, 3)}")

else:
    print("Number isn't 1 or 2 or 3")
