from .__init__ import *
import math


def circumferenceCircle(maxRadius=100, format='string'):
    r = random.randint(0, maxRadius)
    circumference = 2 * math.pi * r

    if format == 'string':
        problem = f"Circumference of circle with radius {r}"
        return problem, circumference
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, circumference


circumference = Generator("Circumference", 104, circumferenceCircle,
                          ["maxRadius=100"])
