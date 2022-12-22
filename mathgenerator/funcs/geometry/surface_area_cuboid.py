from ...generator import Generator
import random


def gen_func(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)
    ans = 2 * (a * b + b * c + c * a)

    problem = f"Surface area of cuboid with sides of lengths: ${a}{unit}, {b}{unit}, {c}{unit}$ is"
    solution = f"${ans} {unit}^2$"
    return problem, solution


surface_area_cuboid = Generator("Surface Area of Cuboid", 33,
                                gen_func, ["maxSide=20", "unit='m'"])
