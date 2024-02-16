def func(numbers, power):
    powered_numbers = [num ** power for num in numbers]
    return powered_numbers


result = func([1, 2, 3, 4, 5], 2)
print(result)
