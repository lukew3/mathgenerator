from .__init__ import *


def curvedSurfaceAreaCylinderFunc(maxRadius=49, maxHeight=99, format='string'):
    r = random.randint(1, maxRadius)
    h = random.randint(1, maxHeight)
    csa = float(2 * math.pi * r * h)
    formatted_float = round(csa, 2)  # "{:.5f}".format(csa)

    if format == 'string':
        problem = f"What is the curved surface area of a cylinder of radius, {r} and height, {h}?"
        solution = f"CSA of cylinder = {formatted_float}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, h, formatted_float


curved_surface_area_cylinder = Generator("Curved surface area of a cylinder",
                                         95, curvedSurfaceAreaCylinderFunc,
                                         ["maxRadius=49", "maxHeight=99"])
