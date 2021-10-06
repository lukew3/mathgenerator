from .__init__ import *


def surfaceAreaCuboid(maxSide=20, unit='m', format='string'):
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)
    ans = 2 * (a * b + b * c + c * a)

    if format == 'string':
        problem = f"Surface area of cuboid with sides = {a}{unit}, {b}{unit}, {c}{unit} is"
        solution = f"{ans} {unit}^2"
        return problem, solution
    elif format == 'latex':
        return "Latex unavailable"
    else:
        return a, b, c, ans, unit


surface_area_cuboid = Generator("Surface Area of Cuboid", 33,
                                surfaceAreaCuboid, ["maxSide=20", "unit='m'"])
