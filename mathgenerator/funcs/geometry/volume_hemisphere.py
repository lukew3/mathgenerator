from ...__init__ import Generator
import random
import math


def gen_func(maxRadius=100, format='string'):
    r = random.randint(1, maxRadius)
    ans = round((2 * math.pi / 3) * r**3, 3)

    if format == 'string':
        problem = f"Volume of hemisphere with radius {r} m = "
        solution = f"{ans} m^3"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, ans


volume_hemisphere = Generator("Volume of Hemisphere", 117, gen_func,
                              ["maxRadius=100"])
