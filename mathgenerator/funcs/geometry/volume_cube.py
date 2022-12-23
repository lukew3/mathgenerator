from ...generator import Generator
import random


def gen_func(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    ans = a**3

    problem = f"Volume of cube with a side length of ${a}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


volume_cube = Generator("Volume of Cube", 35, gen_func,
                        ["maxSide=20", "unit='m'"])
