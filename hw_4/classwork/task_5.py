hours = int(input("Please enter any count of day hours: "))

if hours == 24:
    hours = 0

if hours in range(0, 6):
    print("Good Night!")

elif hours in range(6, 13):
    print("Good Morning America!")

elif hours in range(13, 17):
    print("Good day!")

elif hours in range(17, 24):
    print("Good Evening!")

else:
    print("Your input isn't in range from 0 to 24")
