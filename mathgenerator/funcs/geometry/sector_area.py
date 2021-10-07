from .__init__ import *


def gen_func(maxRadius=49, maxAngle=359, format='string'):
    r = random.randint(1, maxRadius)
    a = random.randint(1, maxAngle)
    secArea = float((a / 360) * math.pi * r * r)
    formatted_float = "{:.5f}".format(secArea)

    if format == 'string':
        problem = f"Given radius, {r} and angle, {a}. Find the area of the sector."
        solution = f"Area of sector = {formatted_float}"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, a, formatted_float


sector_area = Generator("Area of a Sector", 75, gen_func,
                        ["maxRadius=49", "maxAngle=359"])
