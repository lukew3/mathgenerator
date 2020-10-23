from .__init__ import *


def curvedSurfaceAreaCylinderFunc(maxRadius=49, maxHeight=99):
    r = random.randint(1, maxRadius)
    h = random.randint(1, maxHeight)
    problem = f"What is the curved surface area of a cylinder of radius, {r} and height, {h}?"
    csa = float(2 * math.pi * r * h)
    formatted_float = round(csa, 2)  # "{:.5f}".format(csa)
    solution = f"CSA of cylinder = {formatted_float}"
    return problem, solution


curved_surface_area_cylinder = Generator(
    "Curved surface area of a cylinder", 95,
    "What is CSA of a cylinder of radius, r and height, h?", "csa of cylinder",
    curvedSurfaceAreaCylinderFunc)
