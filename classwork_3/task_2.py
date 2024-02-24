def recursive_sum(a, b):
    if a > b:
        return 0
    else:
        return a + recursive_sum(a + 1, b)


print(recursive_sum(1, 4))
