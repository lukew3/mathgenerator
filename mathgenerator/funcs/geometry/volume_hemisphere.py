from ...generator import Generator
import random
import math


def gen_func(maxRadius=100):
    r = random.randint(1, maxRadius)
    ans = round((2 * math.pi / 3) * r**3, 3)

    problem = f"Volume of hemisphere with radius ${r} m =$ "
    solution = f"${ans} m^3$"
    return problem, solution


volume_hemisphere = Generator("Volume of Hemisphere", 117, gen_func,
                              ["maxRadius=100"])
