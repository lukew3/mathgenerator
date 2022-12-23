import random
import math


def degree_to_rad(max_deg=360):
    """Degrees to Radians"""
    a = random.randint(0, max_deg)
    b = (math.pi * a) / 180
    b = round(b, 2)

    problem = f"Angle ${a}$ degrees in radians is: "
    solution = f'${b}$'
    return problem, solution
