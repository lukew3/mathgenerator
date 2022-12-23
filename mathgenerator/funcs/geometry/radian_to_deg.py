from ...generator import Generator
import random
import math


def gen_func(max_rad=6.28):
    a = random.randint(0, int(max_rad * 100)) / 100
    b = round((180 * a) / math.pi, 2)

    problem = f"Angle ${a}$ radians in degrees is: "
    solution = f'${b}$'
    return problem, solution


radian_to_deg = Generator("Radians to Degrees", 87, gen_func,
                          ["max_rad=6.28"])
