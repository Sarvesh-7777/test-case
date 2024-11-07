import math

def is_numeric(value):
    """
    Check if the input is a number (int or float). If it's not, raise a TypeError.
    """
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be a numeric value.")

def check_positive(value):
    if value < 0:
        raise ValueError("Input must be a non-negative value.")

def sin(angle_in_degrees):
    is_numeric(angle_in_degrees)
    return math.sin(math.radians(angle_in_degrees))

def cos(angle_in_degrees):
    is_numeric(angle_in_degrees)
    return math.cos(math.radians(angle_in_degrees))

def tan(angle_in_degrees):
    is_numeric(angle_in_degrees)
    return math.tan(math.radians(angle_in_degrees))

def sqrt(value):
    is_numeric(value)
    check_positive(value)
    return math.sqrt(value)

def log(value):
    is_numeric(value)
    check_positive(value)
    return math.log(value)

def exp(value):
    is_numeric(value)
    return math.exp(value)
