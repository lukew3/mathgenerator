from ...generator import Generator
import random


def gen_func(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)
    ans = a * b * c

    problem = f"Volume of cuboid with sides = ${a}{unit}, {b}{unit}, {c}{unit}$ is"
    solution = f"${ans} {unit}^3$"
    return problem, solution


volume_cuboid = Generator("Volume of Cuboid", 36, gen_func,
                          ["maxSide=20", "unit='m'"])
