import random
import math


def surface_area_cone(maxRadius=20, maxHeight=50, unit='m'):
    """Surface area of a cone"""
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)

    slopingHeight = math.sqrt(a**2 + b**2)
    ans = int(math.pi * b * slopingHeight + math.pi * b * b)

    problem = f"Surface area of cone with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution
