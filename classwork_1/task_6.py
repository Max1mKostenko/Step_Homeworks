from math import factorial


def func(param):
    return [factorial(i) for i in param]


print(func([i for i in range(1, 11)]))
