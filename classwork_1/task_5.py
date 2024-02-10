def func(param):
    inp = int(input("Please enter any number to find in the list: "))
    if inp in param:
        return f"{inp} in the list"
    return "your number isn't in list"


print(func([i for i in range(-10, 11)]))
