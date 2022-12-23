import random
import math


def volume_cylinder(maxRadius=20, maxHeight=50, unit='m'):
    """Volume of a cylinder"""
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(math.pi * b * b * a)

    problem = f"Volume of cylinder with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution
