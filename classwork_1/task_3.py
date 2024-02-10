def func(param):
    print(param)
    print(len([i for i in param if i % 2 == 0]))
    print(len([i for i in param if i % 2 != 0]))
    print(len([i for i in param if i > 0]))
    print(len([i for i in param if i < 0]))


func([i for i in range(-10, 11)])

