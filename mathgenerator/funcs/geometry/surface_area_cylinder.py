from .__init__ import *


def gen_func(maxRadius=20, maxHeight=50, unit='m', format='string'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(2 * math.pi * a * b + 2 * math.pi * b * b)

    if format == 'string':
        problem = f"Surface area of cylinder with height = {a}{unit} and radius = {b}{unit} is"
        solution = f"{ans} {unit}^2"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, ans, unit


surface_area_cylinder = Generator("Surface Area of Cylinder", 34,
                                  gen_func,
                                  ["maxRadius=20", "maxHeight=50", "unit='m'"])
