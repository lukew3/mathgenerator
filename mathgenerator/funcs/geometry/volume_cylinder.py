from ...generator import Generator
import random
import math


def gen_func(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(math.pi * b * b * a)

    problem = f"Volume of cylinder with height $= {a}{unit}$ and radius $= {b}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


volume_cylinder = Generator("Volume of cylinder", 37, gen_func,
                            ["maxRadius=20", "maxHeight=50", "unit='m'"])
