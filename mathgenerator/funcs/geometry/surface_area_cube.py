from .__init__ import *


def surfaceAreaCube(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    problem = f"Surface area of cube with side = {a}{unit} is"
    ans = 6 * a * a
    solution = f"{ans} {unit}^2"
    return problem, solution


surface_area_cube = Generator("Surface Area of Cube", 32,
                              "Surface area of cube with side a units is",
                              "b units^2", surfaceAreaCube)
