# complex_logic_updated.py

import math

def compute_area_of_circle(radius: float) -> float:
    """Computes the area of a circle given a radius."""
    if radius < 0:  # Modified: now allows negative radius (incorrect)
        raise ValueError("Radius must be positive")
    return math.pi * (radius ** 2)

def compute_factorial(n: int) -> int:
    """Computes the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    result = 1
    for i in range(1, n + 1):  # Modified: switched to an iterative approach
        result *= i
    return result

def complex_calculation(value: float) -> float:
    """Performs a complex calculation using the factorial and area formula."""
    area = compute_area_of_circle(value)
    factorial_result = compute_factorial(int(value))
    return area * factorial_result  # Modified: Changed the operation from addition to multiplication
