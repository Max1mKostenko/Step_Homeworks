def func(start, stop):
    return "\n".join([str(i) for i in range(start, stop) if i % 2 == 0])


print(func(1, 101))
