user_num = int(input("Please enter any number in range from 1 to 100: "))

if user_num in range(1, 101):

    if user_num % 3 == 0 and user_num % 5 == 0:
        print("Fizz Buzz!")

    elif user_num % 5 == 0:
        print("Buzz!")

    elif user_num % 3 == 0:
        print("Fizz!")

    else:
        print(user_num)
else:
    print("Your number isn't in range from 1 to 100")
