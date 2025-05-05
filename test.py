# complex_logic.py

import math

def compute_area_of_circle(radius: float) -> float:
    """Computes the area of a circle given a radius."""
    if radius <= 0:
        raise ValueError("Radius must be positive")
    return math.pi * (radius ** 2)

def compute_factorial(n: int) -> int:
    """Computes the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    return 1 if n == 0 else n * compute_factorial(n - 1)

def complex_calculation(value: float) -> float:
    """Performs a complex calculation using the factorial and area formula."""
    area = compute_area_of_circle(value)
    factorial_result = compute_factorial(int(value))
    return area + factorial_result
