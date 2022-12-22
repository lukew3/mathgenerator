from ...generator import Generator
import random


def gen_func(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    ans = 6 * (a ** 2)

    problem = f"Surface area of cube with side $= {a}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


surface_area_cube = Generator("Surface Area of Cube", 32, gen_func,
                              ["maxSide=20", "unit='m'"])
