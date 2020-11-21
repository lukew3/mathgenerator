from .__init__ import *


def volumeCube(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)

    problem = f"Volume of cube with side = {a}{unit} is"
    ans = a * a * a
    solution = f"{ans} {unit}^3"
    return problem, solution


volume_cube = Generator("Volum of Cube", 35,
                        "Volume of cube with side a units is", "b units^3",
                        volumeCube)
