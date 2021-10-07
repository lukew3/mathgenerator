from .__init__ import *


def gen_func(maxRadius=20, maxHeight=50, unit='m', format='string'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    ans = int(math.pi * b * b * a)

    if format == 'string':
        problem = f"Volume of cylinder with height = {a}{unit} and radius = {b}{unit} is"
        solution = f"{ans} {unit}^3"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, ans, unit


volume_cylinder = Generator("Volume of cylinder", 37, gen_func,
                            ["maxRadius=20", "maxHeight=50", "unit='m'"])
