def func(*nums):
    res = 1
    for i in nums:
        res *= i
    return res


print(func(1, 2, 3, 4, 5, 6))


def func_(nums):
    res = 1
    for i in list(nums):
        res *= i
    return res


print(func_([1, 2, 3, 4, 5, 6]))
