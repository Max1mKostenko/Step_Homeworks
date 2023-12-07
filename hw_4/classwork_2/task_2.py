number = int(input("PLease enter six-digit number: "))

if len(str(number)) == 6:
    reverse = str(number)[::-1]

    print(int(reverse.replace(reverse[2:4], reverse[2:4][::-1])))

else:
    print("The number must be six-digit!")
