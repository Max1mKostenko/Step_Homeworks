num1 = int(input("Please enter first num: "))
num2 = int(input("PLease enter second num: "))

list_ = []
if num1 < num2:
    for i in range(num1, num2 + 1):
        if i % 5 == 0 and i % 3 == 0:
            list_.append("Fizz Buzz")
        elif i % 5 == 0:
            list_.append("Buzz")
        elif i % 3 == 0:
            list_.append("Fizz")
        else:
            list_.append(i)
    print(list_)
else:
    print("First num bigger then second")
