import random
import math


def sector_area(maxRadius=49, maxAngle=359):
    """Area of a Sector"""
    r = random.randint(1, maxRadius)
    a = random.randint(1, maxAngle)
    secArea = float((a / 360) * math.pi * r * r)
    formatted_float = round(secArea, 2)

    problem = f"What is the area of a sector with radius ${r}$ and angle ${a}$ degrees?"
    solution = f"${formatted_float}$"
    return problem, solution
