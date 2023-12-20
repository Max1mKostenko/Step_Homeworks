num1 = int(input("Please enter first num: "))
num2 = int(input("PLease enter second num: "))

while num2 <= num1:
    print("The second number mustn't be more than first")
    num1 = int(input("Please enter first num: "))

num = int(input(f"PLease enter any number in range from {num1} to {num2}: "))

while num not in range(num1, num2 + 1):
    print("Your number isn't in range")
    num = int(input(f"PLease enter any number in range from {num1} to {num2}: "))

for i in range(num1, num2 + 1):
    if i == num:
        print(f"!{i}!", end=" ")
    else:
        print(f"{i}", end=" ")
