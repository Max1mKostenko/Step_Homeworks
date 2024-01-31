from random import randint
list_ = [randint(-100, 101) for i in range(100)]
print(list_)
print(min(list_))
print(max(list_))
print(len([i for i in list_ if i < 0]))
print(len([i for i in list_ if i > 0]))
print(list_.count(0))
