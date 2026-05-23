"""
5_7_functions_defaults_and_named.py
Covers: Default values, optional parameters, and named parameters in Python functions.
"""

def greet(name, greeting="Hello", punctuation="!"):
    """
    Greets a person with a custom greeting, defaulting to 'Hello' and '!'.
    Args:
        name (str): The name of the person to greet.
        greeting (str, optional): The greeting word. Defaults to 'Hello'.
        punctuation (str, optional): The punctuation to end the greeting. Defaults to '!'.
    """
    print(f"{greeting}, {name}{punctuation}")

# Using all default values except 'name'
greet("Alice")  # Output: Hello, Alice!

# Overriding the default greeting
greet(greeting="Bob", name="Hi")  # Output: Hi, Bob!

# Overriding all parameters
greet("Charlie", "Welcome", ".")  # Output: Welcome, Charlie.

# Using named parameters (order doesn't matter)
greet(name="Daisy", punctuation="!!!", greeting="Hey")  # Output: Hey, Daisy!!!

# Example of a function with an optional parameter
def add(a, b=0):
    """
    Adds two numbers. The second number is optional and defaults to 0.
    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 0.
    Returns:
        int or float: The sum of a and b.
    """
    return a + b

print(add(5))        # Output: 5
print(add(5, 3))     # Output: 8
print(add(a=2, b=7)) # Output: 9
