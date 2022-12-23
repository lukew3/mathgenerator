from ...generator import Generator
import random
from math import pi


def gen_func(maxRadius=100):
    r = random.randint(0, maxRadius)
    area = round(pi * r * r, 2)

    problem = f'Area of circle with radius ${r}=$'
    return problem, f'${area}$'


area_of_circle = Generator("Area of Circle", 112, gen_func,
                           ["maxRadius=100"])
