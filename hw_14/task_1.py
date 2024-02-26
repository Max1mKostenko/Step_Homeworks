def func(a, b):
    if b == 0:
        return a
    else:
        return func(b, a % b)


num1 = 48
num2 = 18
print("The biggest common divisor", num1, "and", num2, ":", func(num1, num2))
