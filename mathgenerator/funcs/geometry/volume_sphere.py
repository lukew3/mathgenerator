import random
import math


def volume_sphere(maxRadius=100):
    """Volume of a sphere"""
    r = random.randint(1, maxRadius)
    ans = (4 * math.pi / 3) * r**3

    problem = f"Volume of sphere with radius ${r} m = $"
    solution = f"${ans} m^3$"
    return problem, solution
