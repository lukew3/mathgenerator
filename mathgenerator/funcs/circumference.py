from .__init__ import *


def circumferenceCircle(maxRadius=100):
    r = random.randint(0, maxRadius)
    pi = 22/7
    circumference = 2*pi*r
    problem = f"Circumference of circle with radius {r}"
    solution = circumference
    return problem, solution


circumference = Generator("Circumference", 104, "2*pi*r=", "circumference", circumferenceCircle)
