import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func.__name__} ended for a {execution_time:.4f} seconds")
        return result
    return wrapper

@timeit
def example_function():
    time.sleep(2)
    print("FUnction ended")

example_function()
