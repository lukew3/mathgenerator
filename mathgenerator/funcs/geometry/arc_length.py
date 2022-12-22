from ...generator import Generator
import random
import math


def gen_func(maxRadius=49, maxAngle=359):
    radius = random.randint(1, maxRadius)
    angle = random.randint(1, maxAngle)
    angle_arc_length = float((angle / 360) * 2 * math.pi * radius)
    formatted_float = "{:.5f}".format(angle_arc_length)

    problem = f"Given radius, ${radius}$ and angle, ${angle}$. Find the arc length of the angle."
    solution = f"Arc length of the angle $= {formatted_float}$"
    return problem, solution


arc_length = Generator("Arc length of Angle", 108, gen_func,
                       ["maxRadius=49", "maxAngle=359"])
