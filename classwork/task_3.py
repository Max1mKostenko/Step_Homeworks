num1 = int(input("Please enter first num: "))
num2 = int(input("PLease enter second num: "))

print([i for i in range(num1, num2 + 1) if i % 2 == 0])
