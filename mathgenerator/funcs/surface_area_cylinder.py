from .__init__ import *


def surfaceAreaCylinder(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)

    problem = f"Surface area of cylinder with height = {a}{unit} and radius = {b}{unit} is"
    ans = int(2 * math.pi * a * b + 2 * math.pi * b * b)
    solution = f"{ans} {unit}^2"
    return problem, solution


surface_area_cylinder = Generator(
    "Surface Area of Cylinder", 34,
    "Surface area of cylinder with height = a units and radius = b units is",
    "c units^2", surfaceAreaCylinder)
