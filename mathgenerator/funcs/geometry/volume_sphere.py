from ...generator import Generator
import random
import math


def gen_func(maxRadius=100):
    r = random.randint(1, maxRadius)
    ans = (4 * math.pi / 3) * r**3

    problem = f"Volume of sphere with radius ${r} m = $"
    solution = f"${ans} m^3$"
    return problem, solution


volume_sphere = Generator("Volume of Sphere", 61, gen_func,
                          ["maxRadius=100"])
