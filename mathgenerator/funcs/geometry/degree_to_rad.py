from ...generator import Generator
import random
import math


def gen_func(max_deg=360):
    a = random.randint(0, max_deg)
    b = (math.pi * a) / 180
    b = round(b, 2)

    problem = f"Angle ${a}$ degrees in radians is: "
    solution = f'${b}$'
    return problem, solution


degree_to_rad = Generator("Degrees to Radians", 86, gen_func,
                          ["max_deg=360"])
