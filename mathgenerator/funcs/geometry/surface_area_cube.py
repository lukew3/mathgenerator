from .__init__ import *


def gen_func(maxSide=20, unit='m', format='string'):
    a = random.randint(1, maxSide)
    ans = 6 * a * a

    if format == 'string':
        problem = f"Surface area of cube with side = {a}{unit} is"
        solution = f"{ans} {unit}^2"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, ans, unit


surface_area_cube = Generator("Surface Area of Cube", 32, gen_func,
                              ["maxSide=20", "unit='m'"])
