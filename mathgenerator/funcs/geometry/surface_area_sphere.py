from ...generator import Generator
import random
import math


def gen_func(maxSide=20, unit='m'):
    r = random.randint(1, maxSide)
    ans = 4 * math.pi * r * r

    problem = f"Surface area of Sphere with radius $= {r}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


surface_area_sphere = Generator("Surface Area of Sphere", 60,
                                gen_func, ["maxSide=20", "unit='m'"])
