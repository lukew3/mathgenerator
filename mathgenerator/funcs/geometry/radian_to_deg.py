import random
import math


def radian_to_deg(max_rad=6.28):
    """Radians to Degrees"""
    a = random.randint(0, int(max_rad * 100)) / 100
    b = round((180 * a) / math.pi, 2)

    problem = f"Angle ${a}$ radians in degrees is: "
    solution = f'${b}$'
    return problem, solution
