def func(*lists):
    list_ = lists[0].copy()
    list_.extend(lists[1])
    return list_


print(func([1, 2, 3], [4, 5, 6]))
