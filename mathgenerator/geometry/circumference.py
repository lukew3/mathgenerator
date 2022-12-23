import random
import math


def circumference(maxRadius=100):
    """Circumference of Circle"""
    r = random.randint(0, maxRadius)
    circumference = round(2 * math.pi * r, 2)

    problem = f"Circumference of circle with radius ${r} = $"
    return problem, f'${circumference}$'
