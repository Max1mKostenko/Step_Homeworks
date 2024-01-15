from random import randint
list_1, list_2 = [randint(1, 10) for i in range(10)], [randint(1, 10) for x in range(10)]

print(list_1)
print(list_2)

list_3 = list_1.copy()
list_3.extend(list_2)
print(list_3)

print(list(set(list_3)))

print(list(set(list_1)) and list(set(list_2)))

print(list(set(list_1)) or list(set(list_2)))

print([min(list_1), max(list_1), min(list_2), max(list_2)])
