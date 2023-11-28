num1, num2, num3 = (int(input("Please enter first num: ")), int(input("Please enter second num: ")),
                    int(input("Please enter third num: ")))
user_operator = int(input("""Please enter 1(to add),
             2(to multiply): """))

if user_operator == 1:
    print(f"{num1} + {num2} + {num3} = {sum((num1, num2, num3))}")

elif user_operator == 2:
    print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3}")

else:
    print("Number isn't 1 or 2")
