number = int(input("PLease enter six-digit number: "))

if len(str(number)) == 6:
    first = number // 100000
    second = number // 10000 % 10
    third = number % 10000 // 1000
    fourth = number % 1000 // 100
    fifth = number % 100 // 10
    sixth = number % 10

    if sum((first, second, third)) == sum((fourth, fifth, sixth)):
        print("Number is Lucky!")

    else:
        print("Number is Unlucky!")
else:
    print("The number must be six-digit!")
