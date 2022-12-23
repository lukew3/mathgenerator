import random
from math import pi


def area_of_circle(maxRadius=100):
    """Area of Circle"""
    r = random.randint(0, maxRadius)
    area = round(pi * r * r, 2)

    problem = f'Area of circle with radius ${r}=$'
    return problem, f'${area}$'
