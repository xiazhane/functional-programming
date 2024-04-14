import functools
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def log_args_and_return(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log input arguments
        logging.info(f"Calling {func.__name__} with arguments: {args}, {kwargs}")

        # Call the original function
        result = func(*args, **kwargs)

        # Log the return value
        logging.info(f"{func.__name__} returned: {result}")

        return result

    return wrapper

# Example usage:

# Applying the decorator to a function
@log_args_and_return
def add(a, b):
    return a + b

@log_args_and_return
def multiply(x, y):
    return x * y

# Testing the decorated functions
result_add = add(2, 3)
result_multiply = multiply(4, 5)

# Output will be logged to the console based on the configuration
