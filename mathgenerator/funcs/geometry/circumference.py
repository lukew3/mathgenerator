from ...generator import Generator
import random
import math


def gen_func(maxRadius=100):
    r = random.randint(0, maxRadius)
    circumference = round(2 * math.pi * r, 2)

    problem = f"Circumference of circle with radius ${r} = $"
    return problem, f'${circumference}$'


circumference = Generator("Circumference", 104, gen_func,
                          ["maxRadius=100"])
