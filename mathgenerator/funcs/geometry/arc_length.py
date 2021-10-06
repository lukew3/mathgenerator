from .__init__ import *

import math


def arclengthFunc(maxRadius=49, maxAngle=359, format='string'):
    radius = random.randint(1, maxRadius)
    angle = random.randint(1, maxAngle)
    problem = f"Given radius, {radius} and angle, {angle}. Find the arc length of the angle."
    angle_arc_length = float((angle / 360) * 2 * math.pi * radius)
    formatted_float = "{:.5f}".format(angle_arc_length)

    if format == 'string':
        solution = f"Arc length of the angle = {formatted_float}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return radius, angle, formatted_float


arc_length = Generator("Arc length of Angle", 108, arclengthFunc,
                       ["maxRadius=49", "maxAngle=359"])
