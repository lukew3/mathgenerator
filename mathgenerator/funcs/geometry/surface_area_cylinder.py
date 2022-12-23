import random
import math


def surface_area_cylinder(maxRadius=20, maxHeight=50, unit='m'):
    """Surface area of a cylinder"""
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(2 * math.pi * a * b + 2 * math.pi * b * b)

    problem = f"Surface area of cylinder with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution
