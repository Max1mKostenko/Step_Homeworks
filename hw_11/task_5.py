def multiply_numbers_in_range(lower, upper):
    if lower > upper:
        lower, upper = upper, lower
    result = 1
    for num in range(lower, upper + 1):
        result *= num

    return result


lower_bound = 5
upper_bound = 25

result = multiply_numbers_in_range(lower_bound, upper_bound)
print(f"Product of numbers in the range from {lower_bound} to {upper_bound} equal: {result}")
