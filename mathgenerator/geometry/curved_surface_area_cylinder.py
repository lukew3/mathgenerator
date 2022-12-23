import random
import math


def curved_surface_area_cylinder(maxRadius=49, maxHeight=99):
    """Curved surface area of a cylinder"""
    r = random.randint(1, maxRadius)
    h = random.randint(1, maxHeight)
    csa = float(2 * math.pi * r * h)
    formatted_float = round(csa, 2)  # "{:.5f}".format(csa)

    problem = f"What is the curved surface area of a cylinder of radius, ${r}$ and height, ${h}$?"
    solution = f"${formatted_float}$"
    return problem, solution
