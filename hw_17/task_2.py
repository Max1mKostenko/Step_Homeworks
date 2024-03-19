def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

@memoize
def example_function(n):
    print(f"Function returned with argument {n}")
    return n * n

print(example_function(5))
print(example_function(5))
print(example_function(10))
print(example_function(10))
