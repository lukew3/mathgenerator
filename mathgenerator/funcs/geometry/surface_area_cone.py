from .__init__ import *


def gen_func(maxRadius=20, maxHeight=50, unit='m', format='string'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)

    slopingHeight = math.sqrt(a**2 + b**2)
    ans = int(math.pi * b * slopingHeight + math.pi * b * b)

    if format == 'string':
        problem = f"Surface area of cone with height = {a}{unit} and radius = {b}{unit} is"
        solution = f"{ans} {unit}^2"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, ans, unit


surface_area_cone = Generator("Surface Area of cone", 38, gen_func,
                              ["maxRadius=20", "maxHeight=50", "unit='m'"])
