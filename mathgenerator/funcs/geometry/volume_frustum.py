from ...generator import Generator
import random
import math


def gen_func(maxR1=20, maxR2=20, maxHeight=50, unit='m'):
    h = random.randint(1, maxHeight)
    r1 = random.randint(1, maxR1)
    r2 = random.randint(1, maxR2)
    ans = ((math.pi * h) * (r1 ** 2 + r2 ** 2 + r1 * r2)) // 3

    problem = f"Volume of frustum with height $= {h}{unit}$ and $r1 = {r1}{unit}$ is and $r2 = {r1}{unit}$ is "
    solution = f"${ans} {unit}^3$"
    return problem, solution


volume_frustum = Generator("Volume of frustum", 113, gen_func,
                           ["maxR1=20", "maxR2=20", "maxHeight=50", "unit='m'"])
