from ...generator import Generator
import random
import math


def gen_func(maxRadius=49, maxHeight=99):
    r = random.randint(1, maxRadius)
    h = random.randint(1, maxHeight)
    csa = float(2 * math.pi * r * h)
    formatted_float = round(csa, 2)  # "{:.5f}".format(csa)

    problem = f"What is the curved surface area of a cylinder of radius, ${r}$ and height, ${h}$?"
    solution = f"${formatted_float}$"
    return problem, solution


curved_surface_area_cylinder = Generator("Curved surface area of a cylinder",
                                         95, gen_func,
                                         ["maxRadius=49", "maxHeight=99"])
