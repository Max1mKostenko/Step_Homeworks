user_num = float(input("Please enter any number: "))

degree = int(input("Please enter number-degree between 1 and 7: "))

if degree in range(1, 8):
    print(f"{user_num} ** {degree} = {user_num ** degree}")

else:
    print("number isn't in range from 1 to 7.")
