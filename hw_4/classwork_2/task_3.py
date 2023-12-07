month = int(input("Please enter any month number: "))

if month == 12:
    month = 0

if month in range(0, 3):
    print("Winter!")

elif month in range(3, 6):
    print("Spring!")

elif month in range(6, 9):
    print("Summer!")

elif month in range(9, 12):
    print("Autumn!")

else:
    print("Your input isn't in range from 1 to 12")
