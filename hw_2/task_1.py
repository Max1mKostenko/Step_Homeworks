first = int(input("Please enter first number: "))
second = int(input("Please enter second number: "))
third = int(input("Please enter third number: "))

if all(num in range(0, 10) for num in [first, second, third]):
    print(first * 100 + second * 10 + third)
else:
    print("some number isn't in range from 0 to 9")
