from .__init__ import *

import math


def arclengthFunc(maxRadius=49, maxAngle=359):
    Radius = random.randint(1, maxRadius)
    Angle = random.randint(1, maxAngle)
    problem = f"Given radius, {Radius} and angle, {Angle}. Find the arc length of the angle."
    angle_arc_length = float((Angle / 360) * 2 * math.pi * Radius)
    formatted_float = "{:.5f}".format(angle_arc_length)
    solution = f"Arc length of the angle = {formatted_float}"
    return problem, solution


arc_length = Generator("Arc length of Angle", 108,
                       " Given the radius, r and angle, ang. Calculate the arc length of the given angle", "(ang/360) * 2 * pi * r", arclengthFunc)
