from .__init__ import *
from ..__init__ import Generator


def surfaceAreaSphere(maxSide=20, unit='m'):
    r = random.randint(1, maxSide)

    problem = f"Surface area of Sphere with radius = {r}{unit} is"
    ans = 4 * math.pi * r * r
    solution = f"{ans} {unit}^2"
    return problem, solution


surfaceAreaSphereGen = Generator(
    "Surface Area of Sphere", 60,
    "Surface area of sphere with radius = a units is", "d units^2",
    surfaceAreaSphere)
