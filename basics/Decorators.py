

# Timing Function Execution with a Decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        print(f"Execution time: of function {func.__name__}: {end_time - start_time:.4f} seconds")  # Print the execution time
        return result  # Return the result of the original function
    return wrapper


def debugger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)  # Call the original function
        return result  # Return the result of the original function
    return wrapper


def cache(func):
    cache_value = {}
    print(f"Cache initialized for function {func.__name__}")
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]            
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(2)  # Simulate a delay of 2 seconds
    return a + b

# # Example usage of the timer decorator
@timer 
def example_function(n):
    """A sample function that simulates a time-consuming task."""
    total = 0
    for i in range(n):
        total += i ** 2  # Simulate some work by calculating squares
    return total

@debugger
def example_debugger_function(x, y):
    """A sample function to demonstrate the debugger decorator."""
    return x + y

# Call the example function to see the timer in action
result = example_function(1000000)

# Call the example debugger functionto see the debugger in action
debug_result = example_debugger_function(5, 10)

# Call the long running function to see the cache in action
print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(3, 4))


