from .__init__ import *


def volumeCube(maxSide=20, unit='m', format='string'):
    a = random.randint(1, maxSide)
    ans = a**3

    if format == 'string':
        problem = f"Volume of cube with side = {a}{unit} is"
        solution = f"{ans} {unit}^3"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, ans, unit


volume_cube = Generator("Volum of Cube", 35, volumeCube,
                        ["maxSide=20", "unit='m'"])
