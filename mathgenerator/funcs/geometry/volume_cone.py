import random
import math


def volume_cone(maxRadius=20, maxHeight=50, unit='m'):
    """Volume of a cone"""
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(math.pi * b * b * a * (1 / 3))

    problem = f"Volume of cone with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution
