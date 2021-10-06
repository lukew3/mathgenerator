from .__init__ import *


def areaCircle(maxRadius=100, format='string'):
    r = random.randint(0, maxRadius)
    pi = 22 / 7
    area = pi * r * r

    if format == 'string':
        problem = f"Area of circle with radius {r}"
        return problem, str(area)
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, area


area_of_circle = Generator("Area of Circle", 112, areaCircle,
                           ["maxRadius=100"])
