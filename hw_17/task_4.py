def type_check(types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Argument {arg} is not type {arg_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check([int, str])
def example_function(num, text):
    print(f"Number: {num}, String: {text}")


example_function(5, "Hello")

