num1 = int(input("Please enter first num: "))
num2 = int(input("PLease enter second num: "))

if num1 < num2:
    print(" ".join([str(i) for i in range(num1, num2 + 1) if i % 7 == 0]))
else:
    print("First num bigger then second")
