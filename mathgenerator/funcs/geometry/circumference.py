from .__init__ import *
import math


def circumferenceCircle(maxRadius=100):
    r = random.randint(0, maxRadius)
    circumference = 2 * math.pi * r
    problem = f"Circumference of circle with radius {r}"
    solution = circumference
    return problem, solution


circumference = Generator("Circumference", 104, "2*pi*r=", "circumference", circumferenceCircle)
