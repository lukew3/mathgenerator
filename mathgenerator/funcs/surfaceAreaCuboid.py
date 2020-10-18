from .__init__ import *


def surfaceAreaCuboid(maxSide=20, unit='m'):
    a = random.randint(1, maxSide)
    b = random.randint(1, maxSide)
    c = random.randint(1, maxSide)
    
    problem = f"Surface area of cuboid with sides = {a}{unit}, {b}{unit}, {c}{unit} is"
    ans = 2 * (a * b + b * c + c * a)
    solution = f"{ans} {unit}^2"
    return problem, solution
