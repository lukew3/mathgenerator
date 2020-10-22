from .__init__ import *


def sectorAreaFunc(maxRadius=49, maxAngle=359):
    Radius = random.randint(1, maxRadius)
    Angle = random.randint(1, maxAngle)
    problem = f"Given radius, {Radius} and angle, {Angle}. Find the area of the sector."
    secArea = float((Angle / 360) * math.pi * Radius * Radius)
    formatted_float = "{:.5f}".format(secArea)
    solution = f"Area of sector = {formatted_float}"
    return problem, solution


sector_area = Generator("Area of a Sector", 75,
                        "Area of a sector with radius, r and angle, a ",
                        "Area", sectorAreaFunc)
