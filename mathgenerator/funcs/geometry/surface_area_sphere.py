from .__init__ import *


def gen_func(maxSide=20, unit='m', format='string'):
    r = random.randint(1, maxSide)
    ans = 4 * math.pi * r * r

    if format == 'string':
        problem = f"Surface area of Sphere with radius = {r}{unit} is"
        solution = f"{ans} {unit}^2"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return r, ans, unit


surface_area_sphere = Generator("Surface Area of Sphere", 60,
                                gen_func, ["maxSide=20", "unit='m'"])
