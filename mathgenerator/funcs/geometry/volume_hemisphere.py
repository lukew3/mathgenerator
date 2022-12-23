import random
import math


def volume_hemisphere(maxRadius=100):
    """Volume of a hemisphere"""
    r = random.randint(1, maxRadius)
    ans = round((2 * math.pi / 3) * r**3, 3)

    problem = f"Volume of hemisphere with radius ${r} m =$ "
    solution = f"${ans} m^3$"
    return problem, solution
